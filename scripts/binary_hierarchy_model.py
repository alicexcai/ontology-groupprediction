"""
Binary Task Paths Hierarchical Model Implementation

This module adapts the ElasticNet model implementation to use binary task paths 
from the hierarchical task representation instead of the 24D Task Space dimensions.
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import ElasticNetCV, ElasticNet
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from tqdm import tqdm
import warnings

# Import base functions from hierarchymodel
from hierarchymodel import (
    get_rmse, add_interactions, get_rmse_for_enet, custom_r2,
    train_wave_a_enet, test_wave_b_enet, train_wave_a_test_wave_b_enet
)

# Silence warnings
warnings.filterwarnings("ignore")


def load_binary_task_paths_data(data_path="../outputs/", binary_paths_file="../mapping_data/binary_task_paths.csv"):
    """
    Load the binary task paths data and merge with condition-level data.
    
    Args:
        data_path: Path to data directory containing condition level data
        binary_paths_file: Path to binary task paths CSV file
        
    Returns:
        Tuple of (merged_condition_data, train_test_data, binary_iv_sets)
    """
    # Load condition level data 
    df_condition_level_data = pd.read_csv(f'{data_path}condition_level_group_advantage_with_ivs.csv')
    
    # Load binary task paths
    df_binary_paths = pd.read_csv(binary_paths_file)
    
    # Clean up task names to ensure proper matching
    df_binary_paths['Task'] = df_binary_paths['Task'].str.strip()
    df_condition_level_data['task'] = df_condition_level_data['task'].str.strip()
    
    # Merge binary task paths with condition data
    df_merged = df_condition_level_data.merge(
        df_binary_paths.rename(columns={'Task': 'task'}), 
        on='task', 
        how='left'
    )
    
    # Check for missing tasks
    missing_tasks = df_merged[df_merged['Act'].isna()]['task'].unique()
    if len(missing_tasks) > 0:
        print(f"Warning: The following tasks were not found in binary paths data: {missing_tasks}")
        # Drop rows with missing binary path data
        df_merged = df_merged.dropna(subset=['Act'])
    
    # Load train/test data
    with open(f'{data_path}train_test_data.pkl', 'rb') as f:
        train_test_data = pickle.load(f)
    
    # Filter train/test data to only include tasks we have binary paths for
    available_tasks = df_merged['task'].unique()
    
    filtered_train_test_data = {}
    for wave, data in train_test_data.items():
        filtered_train_test_data[wave] = {}
        for split, df in data.items():
            # Filter to only include available tasks
            filtered_df = df[df['task'].isin(available_tasks)].copy()
            
            # Merge with binary task paths
            filtered_df = filtered_df.merge(
                df_binary_paths.rename(columns={'Task': 'task'}),
                on='task',
                how='left'
            )
            
            filtered_train_test_data[wave][split] = filtered_df
    
    # Define binary task paths IV sets
    binary_path_columns = [col for col in df_binary_paths.columns if col != 'Task']
    controls = ["playerCount", "Low", "Medium", "High"]
    
    binary_iv_sets = {
        "Binary Hierarchy": binary_path_columns + controls,
        "Binary Hierarchy (No Controls)": binary_path_columns
    }
    
    return df_merged, filtered_train_test_data, binary_iv_sets


def train_binary_elasticnet_models(train_test_data, iv_sets, output_dir="../outputs/"):
    """
    Train ElasticNet models for binary task paths and comparison baselines.
    
    Args:
        train_test_data: Dictionary containing training and test data for each wave
        iv_sets: Dictionary containing different sets of independent variables
        output_dir: Directory to save model outputs
        
    Returns:
        Dictionary containing trained models and results
    """
    # Initialize results storage
    base_model = {
        "E-Net": {
            "Wave 1": {"strong": None, "weak": None},
            "Wave 2": {"strong": None, "weak": None}
        }
    }
    
    MODELS = {}
    MODEL_R2_RESULTS = {}
    MODEL_RMSE_RESULTS = {}
    
    for iv_set_name in iv_sets.keys():
        MODELS[iv_set_name] = base_model.copy()
        MODEL_R2_RESULTS[iv_set_name] = base_model.copy()
        MODEL_RMSE_RESULTS[iv_set_name] = base_model.copy()
    
    # Train models
    for wave in tqdm(train_test_data.keys(), desc="Waves"):
        for model_type in iv_sets.keys():
            for dv_type in ["strong", "weak"]:
                
                # Get the training and testing data
                wave_a_data = train_test_data[wave]["train"]
                wave_b_data = train_test_data[wave]["test"]
                ivs = iv_sets[model_type]
                
                # Check if we have all required columns
                missing_cols = [col for col in ivs if col not in wave_a_data.columns]
                if missing_cols:
                    print(f"Warning: Missing columns for {model_type}: {missing_cols}")
                    continue
                
                # Train the model and test it
                model, r2 = train_wave_a_test_wave_b_enet(
                    wave_a_data, wave_b_data, dv_type, ivs, 
                    f"{model_type} {dv_type} {wave}", plot=False
                )
                rmse = get_rmse_for_enet(model, wave_b_data, wave_b_data[dv_type], ivs)
                
                # Store the results
                MODELS[model_type]["E-Net"][wave][dv_type] = model
                MODEL_R2_RESULTS[model_type]["E-Net"][wave][dv_type] = r2
                MODEL_RMSE_RESULTS[model_type]["E-Net"][wave][dv_type] = rmse
                
                print(f"Completed: {model_type} - {dv_type} - {wave}")
    
    # Save results
    with open(f'{output_dir}binary_hierarchy_enet_models.pkl', 'wb') as f:
        pickle.dump(MODELS, f)
    with open(f'{output_dir}binary_hierarchy_enet_model_r2_results.pkl', 'wb') as f:
        pickle.dump(MODEL_R2_RESULTS, f)
    with open(f'{output_dir}binary_hierarchy_enet_model_rmse_results.pkl', 'wb') as f:
        pickle.dump(MODEL_RMSE_RESULTS, f)
    
    return MODELS, MODEL_R2_RESULTS, MODEL_RMSE_RESULTS


def load_baseline_results(output_dir="../outputs/"):
    """
    Load existing baseline model results for comparison.
    
    Args:
        output_dir: Directory containing baseline model results
        
    Returns:
        Dictionary containing baseline R2 and RMSE results
    """
    try:
        # Try to load the main model results (Task Space, McGrath, etc.)
        with open(f'{output_dir}model_r2_results.pkl', 'rb') as f:
            main_r2 = pickle.load(f)
        with open(f'{output_dir}model_rmse_results.pkl', 'rb') as f:
            main_rmse = pickle.load(f)
        
        # Also try to load the hierarchical model results if they exist
        hierarchical_r2 = {}
        hierarchical_rmse = {}
        try:
            with open(f'{output_dir}enet_model_r2_results.pkl', 'rb') as f:
                hierarchical_r2 = pickle.load(f)
            with open(f'{output_dir}enet_model_rmse_results.pkl', 'rb') as f:
                hierarchical_rmse = pickle.load(f)
        except FileNotFoundError:
            pass
        
        # Combine both sets of results
        combined_r2 = {**main_r2, **hierarchical_r2}
        combined_rmse = {**main_rmse, **hierarchical_rmse}
        
        return {"r2": combined_r2, "rmse": combined_rmse}
    
    except FileNotFoundError:
        print("Baseline results not found. You may need to run the original models first.")
        return None


def create_comparison_table(binary_results, baseline_results=None):
    """
    Create a comparison table of model performance.
    
    Args:
        binary_results: Results from binary hierarchy models
        baseline_results: Results from baseline models (optional)
        
    Returns:
        pandas DataFrame with comparison results
    """
    comparison_data = []
    
    # Add binary hierarchy results
    for model_type in binary_results["r2"].keys():
        for wave in ["Wave 1", "Wave 2"]:
            for dv_type in ["strong", "weak"]:
                r2 = binary_results["r2"][model_type]["E-Net"][wave][dv_type]
                rmse = binary_results["rmse"][model_type]["E-Net"][wave][dv_type]
                
                comparison_data.append({
                    "Model": f"{model_type}",
                    "Wave": wave,
                    "DV_Type": dv_type,
                    "R2": r2,
                    "RMSE": rmse
                })
    
    # Add baseline results if available
    if baseline_results:
        for model_type in baseline_results["r2"].keys():
            # Get available waves for this model type
            available_waves = list(baseline_results["r2"][model_type]["E-Net"].keys())
            for wave in available_waves:
                for dv_type in ["strong", "weak"]:
                    r2 = baseline_results["r2"][model_type]["E-Net"][wave][dv_type]
                    rmse = baseline_results["rmse"][model_type]["E-Net"][wave][dv_type]
                    
                    comparison_data.append({
                        "Model": f"{model_type} (Baseline)",
                        "Wave": wave,
                        "DV_Type": dv_type,
                        "R2": r2,
                        "RMSE": rmse
                    })
    
    df_comparison = pd.DataFrame(comparison_data)
    return df_comparison


def print_detailed_results(binary_results):
    """
    Print detailed results for binary hierarchy models.
    """
    print("\nBinary Hierarchy Model Performance Summary:")
    print("=" * 60)
    
    for model_type in binary_results["r2"].keys():
        print(f"\n{model_type}:")
        for wave in ["Wave 1", "Wave 2"]:
            for dv in ["strong", "weak"]:
                r2 = binary_results["r2"][model_type]["E-Net"][wave][dv]
                rmse = binary_results["rmse"][model_type]["E-Net"][wave][dv]
                if r2 is not None and rmse is not None:
                    print(f"  {wave} - {dv}: R² = {r2:.4f}, RMSE = {rmse:.4f}")


if __name__ == "__main__":
    # Load data and train models
    print("Loading binary task paths data...")
    condition_data, train_test_data, iv_sets = load_binary_task_paths_data()
    
    print(f"Available IV sets: {list(iv_sets.keys())}")
    print(f"Binary hierarchy dimensions: {len(iv_sets['Binary Hierarchy']) - 4}")  # Subtract controls
    
    print("\nTraining binary hierarchy ElasticNet models...")
    models, r2_results, rmse_results = train_binary_elasticnet_models(train_test_data, iv_sets)
    
    # Package results
    binary_results = {"r2": r2_results, "rmse": rmse_results}
    
    # Print detailed results
    print_detailed_results(binary_results)
    
    # Load baseline results for comparison
    print("\nLoading baseline results for comparison...")
    baseline_results = load_baseline_results()
    
    # Create comparison table
    print("\nCreating comparison table...")
    comparison_df = create_comparison_table(binary_results, baseline_results)
    
    # Save comparison table
    comparison_df.to_csv("../outputs/model_comparison_binary_hierarchy.csv", index=False)
    print("Comparison table saved to ../outputs/model_comparison_binary_hierarchy.csv")
    
    # Display summary
    print("\nModel Comparison Summary:")
    print("=" * 80)
    
    # Group by model and calculate mean performance
    summary = comparison_df.groupby(['Model', 'DV_Type']).agg({
        'R2': ['mean', 'std'],
        'RMSE': ['mean', 'std']
    }).round(4)
    
    print(summary)
    
    print("\nTraining completed successfully!")
