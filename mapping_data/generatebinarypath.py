"""
Binary Path Generator for Task Classification

This script reads task classification paths from CSV and hierarchical node structure from JSON
to create a binary mapping spreadsheet where each task is mapped to all possible nodes
in the hierarchy with 1s and 0s indicating whether the task's path includes that node.
"""

import pandas as pd
import json
import re
from typing import List, Dict, Set


def extract_all_nodes_from_hierarchy(hierarchy: List[Dict]) -> List[str]:
    """
    Extract all unique node names from the hierarchical JSON structure.
    
    Args:
        hierarchy: List containing the hierarchical structure from JSON
        
    Returns:
        List of all unique node names in the hierarchy
    """
    nodes = []
    
    def traverse_nodes(node):
        if isinstance(node, dict):
            if 'name' in node:
                nodes.append(node['name'])
            if 'children' in node:
                for child in node['children']:
                    traverse_nodes(child)
        elif isinstance(node, list):
            for item in node:
                traverse_nodes(item)
    
    traverse_nodes(hierarchy)
    return nodes


def parse_task_path(path_string: str) -> List[str]:
    """
    Parse a task classification path string to extract the sequence of nodes.
    
    Args:
        path_string: String like "Act > [Act on what?] > Act on information > ..."
        
    Returns:
        List of node names in the path
    """
    # Split by ' > ' and clean up each node
    nodes = [node.strip() for node in path_string.split(' > ')]
    return nodes


def create_binary_mapping(tasks_df: pd.DataFrame, all_nodes: List[str]) -> pd.DataFrame:
    """
    Create a binary mapping DataFrame where each task is mapped to all nodes.
    
    Args:
        tasks_df: DataFrame with Task and Classification Path columns
        all_nodes: List of all possible nodes in the hierarchy
        
    Returns:
        DataFrame with Task column and binary columns for each node
    """
    # Initialize the result DataFrame
    result_data = {'Task': tasks_df['Task'].tolist()}
    
    # Add a column for each node, initialized to 0
    for node in all_nodes:
        result_data[node] = [0] * len(tasks_df)
    
    result_df = pd.DataFrame(result_data)
    
    # For each task, set 1s for nodes in its path
    for idx, row in tasks_df.iterrows():
        task_path_nodes = parse_task_path(row['Classification Path'])
        
        # Set 1 for each node that appears in this task's path
        for node in task_path_nodes:
            if node in all_nodes:
                result_df.loc[idx, node] = 1
    
    return result_df


def generate_binary_path_spreadsheet(csv_file: str, json_file: str, output_file: str = None):
    """
    Main function to generate the binary path spreadsheet.
    
    Args:
        csv_file: Path to the CSV file with tasks and classification paths
        json_file: Path to the JSON file with hierarchy structure
        output_file: Path for output CSV file (optional)
    """
    # Read the CSV file
    print("Reading task classification data...")
    tasks_df = pd.read_csv(csv_file)
    print(f"Loaded {len(tasks_df)} tasks")
    
    # Read the JSON file
    print("Reading hierarchy structure...")
    with open(json_file, 'r') as f:
        hierarchy = json.load(f)
    
    # Extract all nodes from the hierarchy
    print("Extracting all nodes from hierarchy...")
    all_nodes = extract_all_nodes_from_hierarchy(hierarchy)
    print(f"Found {len(all_nodes)} unique nodes")
    
    # Create the binary mapping
    print("Creating binary mapping...")
    binary_df = create_binary_mapping(tasks_df, all_nodes)
    
    # Display some statistics
    print(f"\nBinary mapping created:")
    print(f"- Tasks: {len(binary_df)}")
    print(f"- Node features: {len(all_nodes)}")
    print(f"- Total columns: {len(binary_df.columns)}")
    
    # Save to file if output path provided
    if output_file:
        binary_df.to_csv(output_file, index=False)
        print(f"\nBinary path spreadsheet saved to: {output_file}")
    
    # Display sample of the result
    print(f"\nSample of the binary mapping (first 5 tasks, first 10 node columns):")
    sample_cols = ['Task'] + all_nodes[:9]  # Task + first 9 nodes
    print(binary_df[sample_cols].head())
    
    # Show path analysis for first task as example
    if len(tasks_df) > 0:
        first_task = tasks_df.iloc[0]
        first_task_path = parse_task_path(first_task['Classification Path'])
        print(f"\nExample - Path for '{first_task['Task']}':")
        print(f"Raw path: {first_task['Classification Path']}")
        print(f"Parsed nodes: {first_task_path}")
        print(f"Nodes in hierarchy: {[node for node in first_task_path if node in all_nodes]}")
    
    return binary_df, all_nodes


def print_all_nodes(all_nodes: List[str]):
    """Print all nodes in the hierarchy for reference."""
    print(f"\nAll {len(all_nodes)} nodes in the hierarchy:")
    for i, node in enumerate(all_nodes, 1):
        print(f"{i:2d}. {node}")


if __name__ == "__main__":
    # File paths
    csv_file = "20 edited.csv"
    json_file = "20 edited.json"
    output_file = "binary_task_paths.csv"
    
    print("=== Binary Path Generator ===")
    print(f"Input CSV: {csv_file}")
    print(f"Input JSON: {json_file}")
    print(f"Output: {output_file}")
    print("=" * 50)
    
    try:
        # Generate the binary path spreadsheet
        binary_df, all_nodes = generate_binary_path_spreadsheet(csv_file, json_file, output_file)
        
        # Print all nodes for reference
        print_all_nodes(all_nodes)
        
        print("\n=== Generation Complete ===")
        
    except FileNotFoundError as e:
        print(f"Error: Could not find input file - {e}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
