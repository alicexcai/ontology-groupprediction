```
UPDATED DATE: August 14, 2025
```
# The Task Space: A Multidimensional Representation of Team Tasks

**Authors**

Xinlan Emily Hu^ a*, Mark E. Whiting^ a, Linnea Gandhi^ a, Duncan J. Watts^ a, Abdullah Almaatouq^ b*

a The Wharton School, University of Pennsylvania

b Sloan School of Management, Massachusetts Institute of Technology

*^ Correspondence to: xehu@wharton.upenn.edu; amaatouq@mit.edu

**Abstract**

Despite decades of research on teams, even fundamental questions like when interacting groups

outperform individuals remain unresolved. Although multiple factors contribute to this lack of consensus

(from methodological differences to varying contexts) one particularly important source of inconsistency

is task variation. Most studies involve teams working on one specific task or at most a handful of tasks,

yet findings from one task often fail to generalize to others. This generalizability problem stems from the

_incommensurability_ of tasks: although many taxonomies have been proposed, it remains difficult to

quantify how similar or different any task is to any other. Consequently, determining whether a result

acquired in connection with one task will hold for other tasks has remained challenging. Here, we address

this challenge by introducing the “Task Space,” a multidimensional representation that synthesizes 24 task

dimensions, making it possible to measure similarities and differences between tasks. We demonstrate the

Task Space’s utility through a large-scale integrative experiment on group advantage—i.e., the

performance gain due to group interaction relative to an equivalent number of individuals working

independently. The experiment involved 1,231 participants working on 20 different tasks at three

complexity levels, either individually or in groups of three or six, resulting in 5,972 observations across

180 unique experimental conditions. Our results reveal striking heterogeneity in group advantage, with

outcomes ranging from one-third to 1.6 times the performance of the best individual, depending on the

task. The Task Space significantly outperforms existing taxonomies in predicting this group advantage.

Analysis of our predictive models reveals that task features interact in important ways (e.g., the benefit of

creativity depends critically on whether the task has demonstrably correct answers). By making tasks

commensurable, our framework enables researchers to move beyond asking whether groups “work better”

to identifying the specific, task-related conditions under which they do and do not work.

_Keywords_ : teams, groups, tasks, experiment design, taxonomy, representation, generalizability,

commensurability


**1. Introduction**

Teams are ubiquitous. They play key roles in areas as diverse as the military (Goodwin et al. 2018),

healthcare (Valentine et al. 2015), and corporate governance (Barrick et al. 2007 ; Peterson et al. 1998).

However, the variety in both teams and their related research has made it difficult to produce a coherent

science of teamwork. Hollenbeck, Beersma, and Schouten (2012) astutely observed that “the diversity of

this expanding research ... creates certain challenges. Perhaps the greatest is the problem it causes in

generating a cumulative knowledge base for meaningfully integrating and aggregating results across

studies.”

Consider, for example, the question of when groups outperform individuals—what researchers call _group_

_advantage_ or _team synergy_ (Larson 2010). This question is at the heart of lively scholarly debates in the

social and behavioral sciences (Hill 1982; Larson 2010; Almaatouq, Alsobay, et al. 2021) and is crucial

for managerial decisions in organizations (Barrick et al. 2007). Although it is generally accepted that

groups can exhibit performance advantages, the specific conditions under which this occurs remain

unclear (Almaatouq, Griffiths, et al. 2024a). As with many questions in team research, there is not so

much a single answer as there is a collection of phrases starting with “it depends,” with researchers

identifying the task being performed as a key determinant of group performance (Morris 1966; McGrath

1984; Steiner 1972; Stewart and Barrick 2000; Herold 1978; Whiting et al. 2019; Meluso and

Hébert-Dufresne 2023). For example, Husband (1940)’s early study of puzzle-solving teams concluded

that groups are better for tasks “requiring definite originality and insight,” but not for those that are

predictable and routine. More recent work by Almaatouq et al. (2021), using a room assignment task,

demonstrated that groups outperform individuals only when task complexity is sufficiently high.

Meanwhile, other studies show conflicting patterns: groups are advantageous at intellective tasks where

members can verify correct answers—the “truth wins” phenomenon (Laughlin et al. 2006)—but generate

fewer creative ideas than individuals working separately (Mullen et al. 1991; Diehl and Stroebe 1987).

While researchers have long recognized that tasks matter, the problem is that tasks are complex and

multidimensional, and we lack a systematic way to quantify which specific attributes drive these different

outcomes. And though there have been multiple proposed frameworks for classifying tasks (McGrath

1984; Shaw 1963; Steiner 1972; Laughlin and Ellis 1986), these classifications not only rely on overly

broad categories but also lack consensus about which task dimensions are most important (Larson 2010).

Categorizing tasks into broad, unidimensional “types”—such as “Intellective” and

“Maximizing”—obscures sources of variation that are not captured by the category label. For example,

while completing a crossword puzzle and solving an algebraic equation are both “Intellective” tasks that


involve identifying a correct answer, they differ in other respects that could meaningfully impact group

outcomes (such as the degree of mathematical reasoning required, the role of vocabulary knowledge, or

the potential for collaborative problem-solving). Making matters worse, task frameworks can describe the

same task in different, often incomparable, terms. According to McGrath (1984), both crossword puzzles

and algebra questions are Intellective tasks; under Zigurs et al. (1999)’s framework, the algebra question

is a “Simple Task” because it has only one unambiguously correct answer, while the crossword puzzle is a

“Problem Task” because involves uncertainty about which words might fit a given clue. Thus, two tasks

that appear equivalent in one framework can be placed in entirely different categories in another.

The lack of a common set of dimensions ( _incommensurability_ ) makes it difficult to create meaningful

comparisons across studies; when a finding from one setting fails to generalize to another (Chang et al.

2021; Yarkoni 2022; Almaatouq, Griffiths, et al. 2024a) it is unclear whether to attribute the discrepancy

to replication failure, methodological error, or sufficiently dissimilar tasks. Enabling commensurability

across tasks—and allowing knowledge to be better integrated into a cohesive whole—is therefore critical

to the research of teams.

To fill this gap, we introduce a 24-dimensional design space of team tasks, which we call the “Task

Space,” that synthesizes task taxonomies^1 from the literature to date. Each dimension in the space

represents a specific construct motivated by prior research (e.g., McGrath 1984 ; Shaw 1963 ; Steiner 1972 ;

Laughlin and Ellis 1986 ). By positioning tasks as points in this multidimensional space rather than forcing

them into broad categories, we enable quantitative comparisons between any two tasks. We additionally

label a repository of 102 tasks sourced from empirical literature on team performance, creating what we

call the “Task Map.” The Task Map serves as the basis of a large-scale study that demonstrates our

approach, as well as a standalone contribution for use in future research.

The Task Space solves the incommensurability problem: researchers can now quantify how similar

Husband's puzzle-solving tasks are to Almaatouq's room assignment task, and determine whether

conflicting findings reflect genuine boundary conditions or incomparable contexts. Beyond reconciling

past findings, the Task Space enables systematic research design (Almaatouq, Griffiths, et al. 2024a),

allowing researchers to select tasks with specific features or sample tasks that are maximally different.

Finally, the Task Space can serve a living resource, in which new tasks and dimensions will be added as

(^1) In some cases, prior work refers to taxonomies, whereas in other cases it refers to typologies. Although there are subtle
differences between taxonomies and typologies (see: Bailey 1994; 1989), the terms are often used interchangeably. Reflecting
this common practice, we will use the term “taxonomy” to refer to both concepts, noting also that the technical differences are not
relevant to our framework.


our understanding evolves. This unified framework allows future discoveries to be seamlessly integrated

into the cumulative knowledge base rather than be viewed as isolated findings.

We empirically demonstrate the utility of the Task Space through a large-scale integrative experiment

examining whether groups outperform individuals. After systematically sampling 20 diverse tasks from

the Task Map, we build each task at three levels of complexity and randomly assign 1,231 participants to

work either individually, in groups of three, or in groups of six. This design resulted in 5,972 observations

across 180 unique experimental conditions. Our experiment reveals striking heterogeneity in group

advantage depending on the task context. Critically, the heterogeneity is predictable—by using

dimensions from the Task Space in predictive models, we achieve significantly higher performance than

models relying on traditional categorical approaches. These findings illustrate how the Task Space can

transform isolated, task-specific findings into cumulative knowledge about when and why it is

advantageous to hire a team.

**2. Background**

The Task Space extends a long history of prior work that has examined the key categories or features of

tasks and that has produced numerous competing taxonomies (e.g., Cohen and Bailey 1997 ; Driskell,

Salas, and Hogan 1987 ; Wildman et al. 2012 ; Shaw 1963 ; Wood 1986 ; Hackman 1968 a; Peterson et al.

2001 ; McCormick, Jeanneret, and Mecham 1972 ; Tushman 1979). In our review of the literature, we

identified 15 such taxonomies (Supplementary Materials, Appendix A) and found significant

heterogeneity across them. More problematically, while each taxonomy, when viewed in isolation, offers

a plausible account of how tasks differ from each other, when viewed in aggregate, the accounts are not

collectively coherent — partly because they focus on different attributes of tasks and partly because they

adopt different definitions of a “task” to begin with. For example, some frameworks emphasize the task’s

stimulus material (e.g., Hackman 1968 a; McGrath 1984 ), while others focus on the primary goal (e.g.,

Laughlin and Ellis 1986), the work process (e.g., Steiner 1972), the required skills (e.g., Roby and

Lanzetta 1958 ; Fleishman 1975 ), and even the level of participants’ interest in the task (Shaw 1963).

These divergent perspectives reflect three related sources of incommensurability: the conceptual paradigm

in defining a task; the data source or setting; and the level of detail required to describe the task. The first

source, as noted by Hackman (1968b), is that researchers use different conceptual paradigms when

describing a “task.” Some researchers use a _task qua task_ paradigm, which defines task dimensions purely

based on the stimulus material. Others focus on how participants interact with the material— _task as_

_behavior requirement_ emphasizes the behaviors that successful participants should achieve, while _task as_

_behavior description_ focuses on the typical behaviors that participants display. Still others adopt a _task as_


_ability requirement_ approach, focusing on personal characteristics that influence how participants

approach the task. These different paradigms naturally require different types of information: a _task qua_

_task framework_ needs only details about the stimulus itself, while other approaches might require

participant demographic information or empirical data on typical participant reactions.

A second source of incommensurability is that taxonomies draw on data from different settings, and

consequently make different assumptions about the nature of the task and the individuals completing it.

Some frameworks are oriented towards the laboratory (e.g., Hackman 1968 a; Shaw 1963 ; Steiner 1972 ;

McGrath 1984 ) and therefore assume that tasks are short, self-contained activities with clear goals. Others

are oriented towards real work environments (e.g., Hackman and Oldham 1975 ; Driskell, Salas, and

Hogan 1987 ; Peterson et al. 2001 ; Wildman et al. 2012 ) where tasks tend to be more open-ended and

place greater demands on employees’ abilities and skills. Still other frameworks synthesize features from

both lab and field contexts (e.g., Driskell, Salas, and Hogan 1987). Categorization of tasks can therefore

be highly specific to the setting being studied, such as “Basic Research” versus “Applied Research”

(Tushman 1979) or “Managing Others,” “Advising Others,” and “Human Service” (Wildman et al. 2012).

Finally, different task frameworks describe their features using varying levels of detail. While some

frameworks require information about the exact mechanics of performing a task—down to the precise

number of actions involved (Wood 1986) and the duration of each stimulus (Fleishman 1975)—others

place tasks into broad categories, such as “Production,” “Discussion,” and “Problem-Solving” in

Hackman (1968a) and the eight categories in McGrath (1984). Although a general description (“this task

is about solving math problems”) would be enough to categorize a task as “Problem-Solving” in

Hackman’s framework, Wood would require additional implementation details to determine the problem’s

complexity.

Thus, differences in _paradigms_ , _settings_ , and _levels of detail_ often result in task frameworks that cannot

“speak to one another.” Given the same details regarding two tasks, one framework might place the tasks

into the same category; another might place them into opposing categories; and a third framework might

not be able to categorize them at all, because it requires a different set of information or makes a different

assumption about the environment.

Our observation of incommensurability in task frameworks has parallels with other studies of the features

underlying team-related constructs. For example, Hollenbeck, Beersma, and Schouten (2012)’s critique of

using taxonomies to determine “types” of teams also applies to our case (“types” of tasks). In fact,

substituting the word “team” for “task,” their passage almost exactly replicates our point:


```
The literature on teams [ tasks ] proposes a dizzying array of different team [ task ] types, even
```
```
though the number of actual underlying dimensions used as building blocks to construct team
```
```
[ task ] types is limited. This state of affairs impedes the meaningful accumulation of results across
```
```
studies and, in general, makes it very difficult for researchers or consumers of research to answer
```
```
the question, “What kind of team [ task ] is this?”
```
In Section 3, we seek to resolve task frameworks’ incommensurability by building a flexible design space

of tasks. First, we describe our multidimensional approach, in which each task is allowed to have a

non-zero association with any task dimension, rather than being assigned to a single “category” or “type.”

Second, we define two related but distinct notions of a task (the _task class_ and _task instance_ ), allowing us

to clarify issues around the conceptual paradigm and level of detail. Finally, we identify a set of 24

dimensions that are relevant at the level of the task class, and we describe our methods for evaluating a

task along these dimensions. By positioning tasks within our 24-dimensional design space, we produce a

unified answer for how similar or different two tasks are.

**3. Introducing the Task Space: Design and Construction**

3.1. Representing Tasks as Vectors in Multidimensional Space

In the Task Space, each task is represented as a vector with _M_ elements, where each element corresponds

to the task’s value on one of _M_ dimensions. A collection of _N_ tasks can thus be represented as an 𝑁 ×𝑀

matrix, where each row is a task and each column is an attribute of the task (Figure 1, left panel). This

representation enables researchers to compute distances or similarities between tasks using standard

metrics (e.g., Euclidean distance, cosine similarity), and to identify clusters of related tasks,

systematically sample tasks for experiments, and quantify semantic relationships (Figure 1, right panel).

The vector representation integrates a variety of proposed task constructs while making few additional

assumptions. For example, unlike in McGrath (1984), we do not assume mutually exclusive or

collectively exhaustive categories, nor do we assume any particular topological structure (e.g., a

circumplex). Reading the matrix in Figure 1, we can see how different frameworks would describe each

task. For instance, “Writing Story” would not be considered a Maximizing task according to Steiner

(1972), and hence the row corresponding to this task has a value of 0 in the column corresponding to the

Maximizing dimension. In contrast, the Shopping Plan is (almost by definition) a Planning task according

to McGrath (1984); thus, the row corresponding to this task has a value of 1 in the Planning dimension.


```
Figure 1. An illustration of the Task Space. Left: Our labeled set of tasks can be thought of as a 102 tasks × 24 dimensional
matrix in which each task is represented as a row vector for which each element (column) is a dimension of the task. Right: Each
row vector in this matrix can also be mapped to a point in 24-dimensional space. This representation makes the Task Space easily
amenable to linear algebra-based analysis (e.g., finding similarity between vectors, clustering, and sampling).
```
The matrix representation makes the Task Space inherently flexible and extensible. Researchers can easily

add new tasks or dimensions, update existing values, or focus on subsets relevant to their research

questions. Because these modifications involve only simple matrix operations, different research groups

can maintain compatible versions while adapting the space to their specific needs.

More concretely, we can think of downstream applications in machine learning terms: theory-informed

task dimensions serve as features to predict outcomes of interest, and the results of these predictions, in

turn, inform the selection and development of task dimensions. This iterative process will progressively

refine the Task Space as more data becomes available. Features that do not predict relevant outcomes may

be removed, and puzzling observations—where tasks occupying the same location have different

outcomes—may suggest the need for new dimensions. New tasks may also inspire the addition of

previously-unexplored dimensions. Figure 2 illustrates this process. Two scientists with different sets of

task dimensions can take the union of their dimensions to create a commensurate space. They then apply

feature engineering techniques—eliminating redundant dimensions, down-selecting subsets, or creating

synthetic dimensions—before using the refined space to predict outcomes of interest. This process, in

turn, creates feedback for refining the task dimensions themselves.


```
Figure 2. An illustration of the iterative theory construction process. Scientists 1 and 2 each begin with different “versions” of the
Task Space; Scientist 1’s version is a two-dimensional space with features A and B, while Scientist 2’s version is a
two-dimensional space with features A1 and B1. To make their versions commensurate, the scientists can simply take the union
of all features, creating a four-dimensional space. The unified space can then be transformed in a variety of ways (“feature
engineering”), which may include eliminating redundant features, down-selecting to a subset of features, creating synthetic
features, or summarizing key factors. The engineered features are then used to predict outcomes of interest. How well task
```
features perform in predicting outcomes will inform additional changes to the task features. For example, task features that do not

```
correlate with any known outcomes can be regarded as irrelevant and removed from the Task Space; task features that
consistently improve model prediction on known outcomes can be retained.
```
In constructing the Task Space, we have deliberately refrained from applying factor analysis or combining

conceptually similar dimensions ex-ante. Because there are many methods of engineering features, our

view is that the features should be evaluated on how well they predict unseen outcomes rather than on

their statistical relationships within the existing database of tasks. This emphasis on empirical validation

mirrors successful dimensional refinement processes in other domains. In early personality psychology,

for example, researchers proposed thousands of potential personality dimensions (Allport and Odbert

1936) before eventually converging on what are now known as the “Big Five” (Goldberg 1993). This

dimension reduction process was driven by a combination of empirical research and vigorous debate

about whether ostensibly similar dimensions captured different underlying constructs. For example,

Hough (1992) argued that Affiliation (socialization preference) and Potency (energy level) should not


have been combined into the single dimension of Extroversion, because they predicted different

work-related outcomes (Potency predicted work success, but Affiliation did not). However, the team

performance field has not yet begun a similar convergence process, because researchers continue to rely

on single taxonomies rather than comparing dimensions across frameworks. In a review of meta-analyses

on team performance in the last 40 years (Supplementary Materials, Appendix H), we found that no

publication classified tasks using more than one taxonomy or typology; some only coded tasks according

to a single dimension (e.g., task interdependence or task complexity); and some included no information

about the task at all. To eventually converge to a potential “Big Five” of task dimensions, scholars should

first test the predictive power of task dimensions across multiple task taxonomies. This process requires

unifying taxonomies into a shared representation; in other words, to construct a Task Map.

3.2. Construction of the Task Map

The Task Map is a repository of 102 tasks that are annotated according to the 24 dimensions of the Task

Space—it is a “worked example” of applying our proposed matrix representation to an initial set of

commonly used tasks and frameworks. This section considers the construction of the map in terms of its

dimensions (columns), tasks (rows), and ratings (cells).

_3.2.1. Dimensions (Columns)._ To establish explicit criteria for the dimensions we include in the Task Map,

we introduce the notion of a _task class_ and _task instance_. A _task class_ , following the task definitions by

Larson (2010) and Hackman (1968), represents the general blueprint of a task, as characterized by its

stimuli and goals. For example, tasks in the Room Assignment class involve a set of students, rooms, and

constraints (the stimuli), in which the students must be optimally allocated (the goal). Importantly,

however, there may be many variations within the class—a “low complexity” version might involve

assigning students to rooms under only one constraint, while a “high complexity” version might involve

dozens of students, rooms, and constraints. We call these variations _task instances_.

This definition clarifies a key issue with existing taxonomies, in which there is no explicit consensus

about the boundaries of a task, leading various frameworks to implicitly mix class- and instance-level

attributes. For example, three of the paradigms we reviewed in Section 2 ( _task as behavior requirement_ ,

_task as behavior description_ , and _task as ability requirement_ ) implicitly operate at the instance level, as

they require specific details about the participants and their reactions to the stimuli. Meanwhile, the _task_

_qua task_ paradigm, which focuses on the stimuli alone, can operate at either the class or instance levels,

depending on whether the dimensions are general (e.g., does this task involve solving a problem?) or

specific (e.g., how many operations does it take to complete the problem?).


Class- and instance-level features require different levels of information. Class-level features represent the

most general level of detail; they are stable regardless of who completes the task, how they choose to

complete the task, or the format in which the task is presented. Instance-level features comprise all of

these specifics. For example, every Room Assignment Task is an optimization problem, but the level of

complexity, allowable group processes, user interface, and expected behaviors can vary. Following

Larson, we treat class-level features as more “core” than task instance features, and hence restrict the

dimensions that we will use for the Task Map to those describing a task class. This restriction does not

imply that we ignore instance-level attributes; rather, because there are too many variations to

comprehensively describe, we propose that researchers incorporate instance-level attributes as additional

dimensions (in Section 4, we will show an example that controls for task complexity in this manner).

Because tasks in the laboratory and in the field are very different in nature, for convenience we also

restrict our attention to laboratory tasks. Because these tasks have typically been used in the context of

evaluating some aspect of team or group performance, they tend to have well-defined stimuli and goals,

allowing us to demonstrate our method in a setting that is complicated enough to highlight its benefits

while keeping it simple enough to explain. We emphasize, however, that there is nothing about the

method we outline that in principle excludes field tasks, and hence, we expect that it will be possible to

expand the Task Space to include them in the future (see Section 5.4 for more discussion).

Applying these two criteria to the dimensions of the Task Map resulted in 24 dimensions^2 sourced from

five frameworks (McGrath 1984 , Shaw 1963 , Steiner 1972 , Zigurs et al. 1999 , Laughlin and Ellis 1986 ;

see Table 1). Further implementation details can be found in Appendix C, Section C4^3.

_3.2.2. Tasks (Rows)._ We sourced 102 tasks from published papers. Groups and teams are of

interdisciplinary interest, with research spanning management (Ericksen and Dyer 2004 ; Marks, Mathieu,

and Zaccaro 2001 ), psychology (J. E. Mathieu et al. 2017 , Salas, Reyes, and McDaniel 2018), computer

science (Harris et al. 2019), sociology (Gross 1954), economics (Weidmann and Deming 2021),

complexity science (Almaatouq, Alsobay, et al. 2021), and other fields. Thus, our aim was not to create a

systematic or fully representative sample of any one field, as each discipline has its own, often

non-overlapping, set of publication venues. Instead, we hand-curated a set of tasks from a diverse set of

(^3) We derived the content of each dimension from the source papers, editing them for clarity and conciseness after pilot testing. In
addition, we wrote a longer elaboration for each question that clarified common misconceptions we found during pilots, which
we also displayed to raters (see Appendix C, Section C2 for piloting procedure and Section C4.3 for elaboration text).
(^2) After completing a review of the literature on task taxonomies, we initially piloted a set of 71 questions. After a substantial
iterative process to ensure reliability and applying exclusions based on the criteria discussed above (task-class focused and
applicable to laboratory studies) our final set included 24 dimensions. As we have noted, we have designed the Task Space such
that it is easy to omit or append additional task dimensions. Therefore, we do not make any claim that this is the final design
space of all tasks, and we welcome contributions by other researchers to further develop the design space (a topic that we will
expand upon later in this paper).


publications across different disciplines, focusing on common task paradigms and influential work. These

include the Collective Intelligence Task Battery (Woolley et al. 2010), forecasting and prediction tasks

(Silver et al. 2021), “classic” tasks used in group studies (Lorge and Solomon 1960), economic games

(Camerer 1997), and others (see Appendix B in the Supplementary Materials). In our repository, each task

is summarized in a standard format that describes the stimuli and goals. We use this repository to

demonstrate the efficacy of applying our task framework in a range of possible research questions in

management and beyond.^4 Section 5 highlights several key applications. We have also publicly released

all data and documentation from our own labeling process,^5 so that future researchers can replicate it for

other domains of interest.

_3.2.3. Ratings (Cells)_. To construct the Task Map, the 102 tasks were rated on 23 dimensions by a panel of

121 Amazon Mechanical Turk workers, who had passed our pre-test with an average score of 84.56%^6.

We initially excluded a 24th dimension, Type 6 (Mixed-Motive), because we were focused on dimensions

applicable to both individual and team tasks; however, this dimension was reintroduced at a later stage

and separately annotated by the author team (see Appendix C4). Over the 23 crowd-rated dimensions,

each task received an average of 23.20 ratings, and ratings across workers were averaged at the question

level for each task and dimension.^7 A rating of 1 indicates that a rater perceived the feature as present,

whereas a 0 indicates that a rater perceived the feature as absent; thus, the end result of the rating process

is a 102 (tasks) × 24 (dimensional) matrix in which all cells contain a real value between 0 and 1, which

we interpret as “the degree to which a task displays a particular feature.” These values are then used to

position tasks in an underlying vector space (for an illustration, please refer to Appendix E2).

```
Table 1: List of Dimensions in the Task Space
```
```
No. Dimension Name Question Text Source
```
```
1 Conceptual-Behavioral Does^ this^ task^ primarily^ require^ physical^ effort,^ as^ opposed^
to primarily requiring mental effort?
McGrath
```
(^7) According to the literature on the wisdom of crowds and prediction markets, aggregating independent opinions generates
accurate estimates for the true value of a quantity, and the arithmetic mean is a robust pooling function (Arrow et al. 2008 , Chen
et al. 2005 , Chen and Li 2012 ).
(^6) All workers were heavily vetted through a three-stage process, in which they were screened for reading comprehension abilities,
provided with step-by-step interactive training, and required to pass a final qualification quiz (see Appendix C, Section C4.1).
(^5) We have released the data, rater training materials, and data cleaning scripts associated with the Task Space at the following
anonymous OSF link: https://osf.io/4pftv/. In addition, we have built a public-facing website (to be linked in the de-anonymized
manuscript) where community members can interact with the data, cluster tasks, and request the addition of new tasks and
dimensions.
(^4) We note that the Task Map is not intended to represent tasks in general. “Representativeness” is determined by one’s research
question, rather than being a universal truth: for example, a researcher studying economic games may be interested in whether the
Ultimatum Game is overrepresented in their field, while another studying conflict may be interested in whether distributive
negotiations are more commonly studied than integrative ones. Answering such questions requires representatively sampling
tasks in those respective fields. However, the method of evaluating tasks according to their dimensions, and positioning them in a
“space” where one can evaluate and draw boundaries between them, remains unchanged.


```
Table 1: List of Dimensions in the Task Space
```
_No. Dimension Name Question Text Source_

```
2 Intellectual-Manipulative*
What is the fraction of physical (as opposed to mental)
effort required for the task? Shaw^
```
```
3 Type 1 (Planning)
```
```
Is this a "planning" task? In other words, is one of the
main purpose(s) of this task to produce a sequence of
concrete steps or actions that an individual can follow to
achieve some goal?
```
```
McGrath
```
```
4 Type 2 (Generate)
```
```
Is this a "generation" or "brainstorming" task? In other
words, is one of the main purpose(s) of this task to
produce a number of ideas or examples, without any
particular action associated with them?
```
```
McGrath
```
```
5 Creativity Input*
```
```
What fraction of the effort required for this task is creative
thinking (as opposed to any other type of effort, whether
physical, logical, etc.)?
```
```
New; Continuous
version of Type 2
(Generate)
```
```
6
Type 3 and Type 4
(Objective Correctness)
```
```
Is there an objectively correct solution to this task that can
be calculated or selected?
McGrath
```
```
7 Type 5 (Cognitive Conflict)
Is one of the main purpose(s) of this task to resolve
people's differences in opinion, perspective, or viewpoint?
McGrath
```
```
8 Type 6 (Mixed-Motive)†^
During this task, group members pursue different interests,
objectives, or goals.
McGrath
```
```
9 Type 7 (Battle)
Can the outcome of this task be described in win/lose
terms?
McGrath
```
```
10 Type 8 (Performance) Does^ the^ task^ have^ an^ all-or-nothing^ outcome?^ In^ other^
words, is it sufficient to just meet a particular standard?
McGrath
```
```
11 Divisible-Unitary
Is it efficient and useful for members of the group to work
on discrete parts (or subtasks) of this activity? Steiner^
```
```
12 Maximizing
```
```
Is the goal (or one of the goals) of this task to try to
achieve doing something as much as possible, as many as
possible, or as quickly as possible?
```
```
Steiner
```
```
13 Optimizing
Is the goal (or one of the goals) of this task to try to
achieve a precise outcome? Steiner^
```
```
14 Outcome Multiplicity
Is there only one "best" solution (or possible solution) to
this task? Shaw,^ Zigurs^ et^ al.^
```
```
15
Solution Scheme
Multiplicity
```
```
Is there only one method for achieving the task, as
opposed to many alternatives for task completion?
Shaw, Zigurs et al.
```
```
16 Decision Verifiability
Can acceptable solutions to this task be demonstrated or
verified to be correct (e.g., by an expert or third-party)?
Laughlin and Ellis
```
```
17 Shared Knowledge
Can this task be written as a "formal model" that an
algorithm could solve?
Laughlin and Ellis
```
```
18 Within-System Solution
Is there enough information in the problem to find a valid
solution? Laughlin^ and^ Ellis^
```

```
Table 1: List of Dimensions in the Task Space
No. Dimension Name Question Text Source
```
```
19 Answer Recognizability
```
```
If someone who is able to solve the problem explains their
answer, would others recognize it as correct without
contest?
```
```
Laughlin and Ellis
```
```
20 Time Solvability
```
```
Is a participant able to come up with a provably correct
solution, assuming sufficient ability, time, motivation, and
resources?
```
```
Laughlin and Ellis
```
```
21 Intellective-Judgmental*
```
```
On a scale of 0 (entirely subjective, with no correct
answer; a judgmental task) to 1 (entirely objective and
demonstrable by pure logic; an intellective task), how
would you classify the extent of demonstrable correctness
of this task?
```
```
Laughlin and Ellis
```
```
22 Conflicting Tradeoffs
```
```
Does completing this task require participants to evaluate
tradeoffs — conflicting possible solutions or conflicting
pieces of information?
```
```
Zigurs et al.
```
```
23
Solution Scheme Outcome
Uncertainty
```
```
When doing this task, will the participants have any
uncertainty about whether their method or solution will
lead to the desired outcome?
```
```
Zigurs et al.
```
```
24 Eureka Question
```
```
Is the solution to the question obvious as soon as it is
proposed — for example, once people see the "trick," they
know how to solve it?
```
```
Laughlin and Ellis
```
```
Table 1. A summary of the 24 dimensions included in the Task Space. 20 of the dimensions were rated on a binary 0-1 scale;
three dimensions, marked with an asterisk (*), were rated on a continuous scale from 0 to 1; one dimension, marked with a cross
```
(†), was hand-coded by researchers (details in Appendix C4). Note that some of these features capture similar or related concepts;

```
we chose to ask separate questions for these concepts so that each question encodes a single idea and because similar concepts
will be loaded onto the same factors (e.g., in factor analysis).
```
**4. Empirical Case Study: A Large-Scale Integrative Experiment of Group Advantage**

We next use the Task Map as part of an _integrative experiment_ (Almaatouq, Griffiths, et al. 2024a), in

which we use task dimensions first to systematically select a diverse set of tasks, and second to predict

group outcomes across the tasks. Our primary outcome is our running example of _group advantage_ : the

performance gain of working in a group, relative to an equivalent number of individuals working

independently. Given heterogeneous findings across several decades of organizational research (e.g.,

Larson 2010; Laughlin et al. 2006; Stasson and Bradshaw 1995; Janis 1971; Diehl and Stroebe 1987;

Steiner 1972), this question is an ideal test case for using the Task Space to integrate experimental results.

4.1 Study Design

To demonstrate the Task Space’s integrative potential, we conducted a large-scale experimental study that

crossed 20 tasks × 3 levels of complexity for each task × 3 group sizes, yielding 180 unique conditions.


We used a sequential design of three experimental “waves,” allowing us to demonstrate use of the Task

Space for out-of-distribution generalization by training models on a set of “seen” tasks, then making

predictions on “unseen” tasks. The first experimental wave contained 10 tasks, while the second and third

waves each contained 5 tasks (details in Appendix F2).

Within each wave, the experiment proceeded identically. Participants were first assigned to work as part

of a collaboration unit of either a single-player, three-player, or six-player group. The unit then completed

a randomly-assigned block sequence of five tasks. Each task had bespoke specifications for parameters

such as timing and the manipulation of complexity. When completing a given task, participants always

experienced four versions: a trivial practice task followed by three graded versions at “low,” “medium,”

and “high” complexity. For example, we increased the difficulty of Word Construction problems by

requiring participants to generate words from lists that had fewer valid word combinations, and we

increased the difficulty of the Room Assignment task by adding more constraints. This within-task

manipulation allowed us to examine whether group advantage emerges only when the task at hand is

sufficiently complex (a phenomenon previously documented in Almaatouq et al. 2021).

In summary, we collected data from 1,231 participants (193 individuals, 134 groups of three, and 106

groups of six), generating 5,972 observations across 180 conditions, where each observation represents

one collaboration unit’s performance on a given task at a given complexity level. The overall study design

is shown in Figure 3.

To contextualize the scale and scope of our demonstration, experimental studies of group performance

routinely study just one task (Almaatouq, Alsobay, et al. 2021; Bavelas 1950; Krackhardt and Stern 1988;

Bahrami et al. 2010; Koriat 2012; Mason and Watts 2011; Shore et al. 2015; Mao et al. 2016; Aggarwal

and Wooley 2019; Straub et al. 2023; Almaatouq et al. 2020; Laughlin et al. 2006; Almaatouq, Alsobay, et

al. 2024), while one of the most ambitious previous studies of which we are aware (Woolley et al. 2010)

comprised ten tasks with fixed complexity level and group size. Indeed, our study is comparable to many

of the largest meta-analyses in the last 20 years (De Dreu and Weingart 2003; Gully et al. 2002; Mullen et

al. 1991; Riedl et al. 2021; Weber and Hertel 2007), but offers several methodological advantages: all

tasks were coded using a consistent framework (the Task Space); all experiments ran under identical

conditions on the Empirica platform (Almaatouq, Becker, et al. 2021); and all participants were recruited

from the same curated panel with detailed demographic information. Additionally, we avoided publication

bias by treating all sampled conditions as informative regardless of statistical significance.


```
Figure 3. Illustration of the experiment design. Panel A shows how we use the Task Space to systematically sample 20 tasks for
the experiment. Panel B shows the experiment design. Participants were randomized into one of three conditions: working
independently, working in interacting groups of three, and working in interacting groups of six (Panel B). Participants
experienced each task at three levels of complexity: “Low,” “Medium,” and “High” (Panel C). In our data, we consider each
observation to be a single collaboration unit (an independent worker or an interacting group) performing a specific task (e.g.,
“Task 1”) at a specific complexity level (e.g., “Low”).
```
4.2 Computing Group Advantage

Our objective is to measure the extent to which interacting groups tend to outperform individuals for a

given task ( _group advantage_ ). This requires us to compare group performance against a baseline of

working independently. Here, following standard practice in the groups literature that distinguishes group

advantage from mere economy of scale (Marquart 1955; Lorge and Solomon 1960; Larson 2010), we

generated “nominal groups” by comparing each interacting group with a randomly permuted aggregation

of individual participants who completed the same task instance. In other words, rather than directly

comparing performance across the group and individual conditions, we treat the individuals as part of a

“pool” from which we sample “nominal groups” that are equivalent in every respect except for the fact

that they did not interact in real time. We then ask, _what advantage does the ability to interact in real time_

_provide, compared to what we’d expect from an identical number of people who worked independently?_


Following Larson (2010) and others (Meslec et al. 2014; Hueffmeier and Hertel 2011), we examine two

variants of group advantage: _strong group advantage_ is the ability of a group to perform better than even

the best-performing individual in a nominal group, and _weak group advantage_ is the ability of a group to

perform better than a randomly-selected member in a nominal group (which, through bootstrapping,

provides an estimate equivalent to average individual performance). Together, these two measures capture

different aspects of collaboration benefits—whether it is worthwhile to hire a group over an average

individual, versus the most competent individual. Details for how we compute these two quantities are

provided in Appendix G1.

4.3 Results

_4.3.1 Group advantage is heterogeneous._ In the analyses that follow, we focus on the 120 group

conditions (3- and 6-person groups), as the 60 individual conditions serve as the baseline for constructing

nominal groups and are already incorporated into the group advantage calculation. Figure 4 shows the

distribution of group advantage across each experimental condition. As expected, the phenomenon of

group advantage is strikingly heterogeneous: across 20 tasks and 120 group conditions, interacting groups

outperformed a random member of the nominal group (weak advantage) in 19 out of 20 tasks and nearly

all experimental conditions (93%), but only outperformed the best member (strong advantage) in 5 tasks

and a minority (26%) of conditions.

This heterogeneity aligns with longstanding observations that group advantage varies with factors such as

the task, complexity, and group size (Larson 2010; Almaatouq, Alsobay, et al. 2021; Bahrami et al. 2010;

Mullen et al. 1991; L. L. Thompson and Wilson 2015; Diehl and Stroebe 1987). However, Figure 4 also

makes the stronger and less obvious point that this heterogeneity does not fall neatly along traditional

lines of task “types.” For example, among the types defined by the McGrath Circumplex, one of the most

influential task typologies, there is almost as much within-type variation as there is overall. A Levene test

of equality in variances shows that the McGrath task types have just as much variance in strong and weak

group advantage as exists in the overall data (Generate, Strong: _W_ (1, 148) = 1.01, _p_ = 0.32; Generate,

Weak: _W_ (1, 148) = 2.14; _p_ = 0.15; Intellective, Strong: _W_ (1, 184) = 3.38, _p_ = 0.07; Intellective, Weak:

_W_ (1, 184) = 0.43; _p_ = 0.51; Performance, Strong: _W_ (1, 130) = 3.61; _p_ = 0.06; Performance, Weak: _W_ (1,

130) = 0.07, _p_ = 0.79); refer to Appendix G3.2 for details. For example, while Advertisement Writing and

Word Construction are both classified as idea generation (i.e., “Type 2” in McGrath’s Group Task

Circumplex), we observe strong group advantage for Word Construction but not for Advertisement

Writing. Similarly, while other judgment tasks (such as Recall Word Lists and Random Dot Motion) show


no strong advantage, the Recall Association task presents a notable exception, with the second-highest

strong group advantage in our corpus.

```
Figure 4. Heterogeneity in group advantage across conditions. Each point represents the observed group advantage at the level of
an experimental condition, which is a tuple of task (y-axis) × level of complexity (color) × group size (point shape; small,
three-person groups are represented by circles and large, six-person groups are represented by crosses). Tasks are grouped by the
experimental wave in which they appeared (top three facets). Error bars represent the analytical 95% confidence intervals (1.96 *
1 standard error) for group advantage in a given condition. Boxes are centered around the mean and show one standard error.
```
This heterogeneity also has important implications for the way in which research on group performance is

interpreted and generalized (Almaatouq, Griffiths, et al. 2024a; 2024b). To illustrate the potential


problem, a researcher focusing solely on the Word Construction or Recall Association tasks (Figure 4; top

of Wave 1 and Wave 3) would reasonably conclude that groups show both strong and weak group

advantage, consistent with prior findings that communication between group members improves on

members’ individual decision making (Bahrami et al. 2010; Koriat 2012). However, if the researcher had

instead chosen to focus on the Whac-a-Mole or Random Dot Motion task (Figure 4; bottom of Wave 1

and Wave 2), they would conclude that groups have no advantage over individuals at all, consistent with

prior work that emphasizes the prominence of process losses (Steiner 1972). Finally, if they were to

examine the Typing and Room Assignment tasks (Figure 4; middle of Wave 1 and Wave 2), they would

find weak, but not strong, group advantage, leading them to conclude that, while groups are superior to a

randomly-selected individual, it is preferable to rely on a small number of experts.

A similar point can be made about interaction effects. For example, Almaatouq et al. (2021) found that

weak group advantage for small groups increases with the complexity of the Room Assignment Task, and

we replicate this effect in our own data using a linear mixed-effects model on the group-level data, with

random effects for the group identifier ( _β_ = 0.114, _p_ < 0.001). Our results, however, show that this pattern

does not hold across all tasks. In fact, we observe the opposite pattern in the Whac-a-Mole task: group

advantage _decreases_ as task complexity increases ( _β_ = -0.107 for strong; _β_ = -0.176 for weak; _p_ < 0.01).

Appendix G4 further explores interaction effects for complexity and group size, and we show that

interaction patterns are heterogeneous across the 20 tasks in our data.

As all these examples illustrate, such substantial between-task heterogeneity implies that generalizations

about group performance based on individual tasks are likely brittle and may not hold even within

seemingly similar task types. Unfortunately, insisting that theoretical claims about group performance can

only be assumed to hold for the exact task or tasks under consideration would effectively prevent any

generalization to new settings, thereby severely undermining a fundamental benefit of theory (Yarkoni

2022). And without a way to reconcile potentially inconsistent results across tasks, the sheer number of

existing results and possible tasks would lead to an unmanageable proliferation of theories, creating

confusion about what is and is not known (Watts 2017; Levinthal and Rosenkopf 2020). Taking a middle

ground, the Task Space allows for an _integrative_ approach (Almaatouq, Griffiths, et al.

2024a)—identifying the “coordinates” (that is, the features) of the task at which groups are likely to

outperform individuals. To quantify the informational content of the task features that we have defined,

we frame this problem as an out-of-sample prediction exercise, where results acquired from one set of

tasks can be used to predict group advantage in entirely new tasks. The associated models can, in turn,

drive theory development by illuminating important relationships between task attributes, complexity

levels, and group sizes.


_4.3.2 Task features predict group advantage._ To assess the predictive value of the Task Space, we use task

features as covariates to predict both strong and weak group advantage. While we detail a more complete

set of models and robustness checks in Appendix G5, here we show three hyperparameter-tuned

ElasticNets, training on the first 15 tasks (Waves 1 and 2) and predicting the final 5 tasks (Wave 3). Our

primary model uses all 24 Task Space dimensions. For comparison, we include two baselines that allow

us to evaluate whether performance gains are attributable to using continuous rather than categorical

dimensions or to expanding the dimensionality of the space beyond that of a single taxonomy. Both

baselines are derived from the McGrath typology (see Appendix G2): the first, “McGrath Categorical,”

encodes McGrath’s task types as dummy variables, and the second, “McGrath Subspace,” uses only the

continuous Task Space dimensions inspired by McGrath’s taxonomy. All models additionally include

controls for the exogenous factors of group size and task complexity, and they are evaluated using root

mean squared error (RMSE).

The Task Space model substantially outperforms both baselines, as shown in Figure 5. For strong group

advantage, it achieves the lowest model error (RMSE = 0.28 vs. 0.31 for McGrath Subspace and 0.37 for

McGrath Categorical). Bootstrapped pairwise comparisons across 250 resamples confirm that the

McGrath Subspace baseline significantly outperforms McGrath Categorical, and the Task Space model

significantly outperforms both (all _p_ < 0.05; Appendix G6.2). For weak group advantage, the Task Space

model again significantly outperforms both baselines (RMSE = 0.58; _p_ < 0.05), while McGrath Subspace

slightly outperforms McGrath Categorical (0.76 vs. 0.77; _p_ = 0.024).

These patterns also suggest that strong group advantage is inherently more predictable than weak group

advantage (baseline RMSE of ~0.3 vs. ~0.8), likely due to lower overall variation in the dependent

variable (Figure 4). Moreover, the same covariates can vary in predictive power across outcomes. For

example, dimensions drawn from McGrath’s taxonomy effectively predict strong group advantage but fail

to do so for weak group advantage. In contrast, the multidimensional Task Space yields effective

predictions for both, underscoring the value of capturing a wider range of task features—beyond the shift

from categorical to continuous dimensions.


```
Figure 5. Scatterplots of predicted versus observed group advantage (training on the first 15 tasks and predicting on the final 5).
Each scatterplot in the figure represents the predictions for one ElasticNet model, with a specific choice of independent variables
(e.g., Task Space, McGrath Subspace, or McGrath Categorical; indicated by hue/row) and dependent variable (e.g., strong versus
weak group advantage; indicated by column). The x -axis shows the true group advantage ratio, while the y -axis shows the
```
model’s prediction. The Task Space yields consistently strong out-of-sample predictions. Note that the ElasticNet model for weak

```
group advantage using McGrath Categorical variables zeroed out all variables, and hence always predicts the mean.
```

_4.3.3 Key Task Space dimensions for predicting group advantage._ To understand which specific task

dimensions drive our prediction results, we next use two complementary approaches to evaluate feature

importance in our primary model. The first method, permutation analysis (Altmann et al. 2010) , measures

the reduction in RMSE after a feature is randomly shuffled. Features that lead to worse RMSE when

permuted are considered more important. The second method, Shapley Additive Explanations (SHAP;

Lundberg and Lee 2017), quantifies the relative influence of each feature on the model’s individual

predictions. While permutation feature importance enables us to assess the magnitude of change on

predictive accuracy, SHAP is useful for inspecting the directional impact of each feature on the model’s

predictions. By applying both methods in parallel, we can better identify which task features are most

important for determining group advantage and also whether these task features help or hurt groups’

expected performance relative to that of individuals.

Figure 6 presents our feature importance analysis, with strong group advantage shown in Panels A and B

and weak group advantage shown in Panels C and D. Features are ordered by their permutation

importance rank. For both outcomes, the most predictive features include the extent to which a task has a

demonstrably correct answer (Demonstrable Correctness), the extent to which a task involves generating

creative ideas (Creative), and the extent to which there is uncertainty about solution correctness (Solution

Scheme Outcome Uncertainty). The first two features each account for nearly 8% of the model's RMSE

for strong group advantage and over 10% of RMSE for weak group advantage. Both features also

positively predict group advantage, as evidenced by the warm-colored points (indicating high feature

values) clustering to the right of the SHAP plot (indicating positive impact on model output).

Beyond these top predictors, importance drops considerably: the third-most important feature, Solution

Scheme Outcome Uncertainty, accounts for less than 5% of the model's RMSE and negatively correlates

with group advantage. Additionally, we find that while some features show consistent patterns across both

dependent variables—whether a task has an all-or-nothing outcome (“Performance” Tasks) ranks among

the least predictive features for both strong and weak group advantage—other features vary in importance

depending on the outcome. For example, whether a task can be divided into subtasks (Divisible-Unitary)

ranks as the second-least important dimension for predicting strong group advantage but is the fifth most

important dimension for predicting weak group advantage.


```
Figure 6. Feature importance among task dimensions for predicting strong (Panels A and B) and weak (Panels C and D) group
advantage. Analyses are for the ElasticNet models, trained on the first 15 tasks (Waves 1-2) and evaluated on the final 5 tasks
(Wave 3). Permutation feature importance is presented in Panels A and C, and SHAP values are presented in Panels B and D,
ordered by their rank in permutation feature importance. In SHAP plots, color indicates whether the feature was high (warm
```
color) or low (cool color) for a given observation, while location relative to the center line indicates whether they are positively

```
(right of center) or negatively (left of center) influential in making a prediction for the observation. Note that, in order to avoid
```
contaminating the permutation analysis with copies of highly correlated features, we create three sets of combined dimensions;

```
“Creative” combines two dimensions related to the extent of creative thinking required; “Demonstrably Correct Answer”
combines seven dimensions related to the extent to which the task has a correct answer that can be verified; and “Physical”
combines two dimensions related to the extent to which a task requires physical effort.
```

We next turn our attention to the top two predictors, Demonstrable Correctness and Creative. The

observation that groups outperform individuals on problems with a correct answer originates from

Laughlin’s early work on social decision schemes and intellective tasks (Laughlin and Ellis 1986;

Laughlin et al. 1975), which posits that, once an individual identifies a correct answer, “truth wins.” The

same notion also underlies contemporary work on estimation and forecasting (Almaatouq et al. 2020;

Becker et al. 2021; Almaatouq et al. 2022). Put another way, if the task has a correct answer that can be

easily verified, it is easy for group members to efficiently search for the answer and to know when one of

them has it right.

Curiously, however, we find that groups outperform individuals at creative tasks, such as Word

Construction and Putting Food Into Categories (which involves generating ideas for grouping food items).

Here, our finding ostensibly contradicts the established result that interacting groups generate fewer ideas

than those working independently (Larson 2010; Mullen et al. 1991; Diehl and Stroebe 1987). However,

this contradiction can be resolved by considering the details of operationalizing group advantage; recall

that, in typical idea generation tasks, researchers compute the nominal group’s performance by combining

the deduplicated raw ideas of all individuals, whereas we compare the group’s final score to the final

score of the best (“strong”) and a randomly-selected (“weak”) individual member of the nominal group.

Group advantage is then represented as a ratio between the interacting group’s score and the nominal

group’s score. In our data, groups in the Putting Food Into Categories task generate on average 1.6 times

as many ideas as the “best” individual from a nominal team; however, this falls short of the theoretical

maximum in which each group member contributes at their individual best level—effectively requiring a

ratio of _n_ (the number of group members) to demonstrate true superiority over simply combining

independent work. In these cases, one might say that the group has an advantage over a single contributor,

but it may not be “worthwhile” to facilitate real-time interaction. However, questions about the threshold

of groupworthiness can be highly context dependent. In a highly competitive market, even a tiny

advantage might be extremely valuable and hence worth assigning to a group; and in different settings,

the cost of hiring a group may differ substantially. Thus, interpreting our results will require careful

consideration of these factors.

In contrast to Demonstrably Correct and Creative tasks, one of the strongest negative predictors of group

advantage is having uncertainty over different possible solutions (Solution Scheme Outcome

Uncertainty). In some sense, tasks with high Solution Scheme Outcome Uncertainty are the inverse of

tasks with high Demonstrable Correctness; rather than having provably correct answers, these tasks have

many plausible solutions. For example, Moral Reasoning, one of the tasks with lowest group advantage,

involves very high uncertainty over the correct answer to a moral quandary. We interpret this result to


mean that groups are often inefficient when navigating uncertainty, a pattern that aligns with groups’

known biases in discussing limited information (Stasser and Titus 1985).

One important note is that, although we directly assign participants to different tasks (for example, Word

Construction versus Advertisement Writing), we do not independently manipulate the underlying features

that characterize these tasks—these are the ratings taken directly from the Task Space. Thus, tasks will

naturally exhibit different combinations of features, and some of this natural variation is useful for

explaining puzzling observations in our data. For example, we observe strong group advantage for Word

Construction, but not for Advertisement Writing, even though both tasks are similar on the Creative

dimension. The puzzle is resolved by recognizing that Word Construction is also high in Demonstrable

Correctness, since it is trivial to verify when one has generated a valid English word, whereas

Advertisement Writing is low in Demonstrable Correctness and high in Solution Scheme Outcome

Uncertainty, as evidenced by the difficulty of predicting click-through rates in headlines (Batista and Ross

2024). Consequently, groups working on Word Construction can much more efficiently combine their

efforts (with each member generating as many words as they can), while groups working on

Advertisement Writing are caught up in discussions about whether an advertisement is appealing or not.

These findings further show that categorizing tasks into “types” fails to tell the whole story. Our

multidimensional approach integrates disparate ideas from across social science (e.g., “truth wins,”

productivity losses) into a cohesive whole.

**5. General Discussion and Future Directions**

In this paper, we introduced the Task Space, a multidimensional representation of tasks. We also provided

the Task Map as a labeled repository of 102 tasks in the 24-dimensional space. The main objective of our

method is to offer a practical solution to the problem that findings from different settings are

incommensurable (Almaatouq et al. 2022 ; Levinthal and Rosenkopf 2020). As we discuss next, our work

is also in conversation with two broader streams of research — systematic sampling of stimuli, and

theories of the middle range — from psychology and sociology respectively.

5.1. Systematically Selecting Study Stimuli

In psychology, theories often deal with broad phenomena: that people seek to conform with groups (Asch

1956), that knowledge of the outcome biases human judgment (Baron and Hershey 1988), and that

previous numerical information anchors new responses (Epley and Gilovich 2006). Each theory may have

a plethora of moderating variables—for example, are people more likely to anchor to larger or smaller

numbers? Do people commit more outcome bias when the stakes are higher?—and the theory is


sometimes silent about the moderator. But just because the theory is silent does not mean the moderator is

irrelevant. To address this concern, a substantial stream of literature in psychology advocates for using

systematic variations in a study’s stimuli to determine the limits of an effect’s generalizability. For

example, rather than study anchoring by giving all participants the same anchor number, the experimenter

might select a range of numbers that represent different categories: very large numbers (10 billion), very

small numbers (0.0001), and other values in between.

An early proponent of this idea, Egon Brunswik, advocated for _representative design_ , or finding a

“representative sampling of [the] situations” in which one intends to generalize their results (Brunswik

1956 , Dhami, Hertwig, and Hoffrage 2004 ). Similarly, Wells and Windschitl (1999) argued that

researchers should engage in _stimulus sampling_ , or using a variety of stimuli within each category of

interest. If one is studying the effects of gender on some phenomenon, for example, using a stimulus of

one man and one woman is “functionally equivalent to conducting an experiment with a sample size of

_n_ =1.” Because only one task represents each category, “what might be portrayed as a category effect

could in fact be due to the unique characteristics of the stimulus selected to represent that category.”

By making it possible to quantify task dimensions, the Task Space extends this line of work and enables

researchers to systematically choose tasks along many dimensions of interest. Rather than studying just

one task, researchers can use the Task Space to “stimulus sample” across different task contexts, and do

so in a far more reproducible way. Possibilities include random exploration (Baribault et al. 2018),

selecting tasks that are maximally far apart, or even adaptive sampling—from using the classic Thompson

sampling technique (W. R. Thompson 1933) to leveraging more recent developments in adaptive

experimental design (Balietti et al. 2021; Eyke et al. 2020; Simonsohn et al. 2024).

5.2. Constructing and Testing “Middle Range” Theories

Our contribution also speaks to longstanding concerns in sociology about the domain specificity of

theories. As Robert Merton once observed, the path to understanding general insights about the social

world is not to seek a single, all-encompassing theory, but to progressively unify “theories of the middle

range”—which are limited in context and scope, yet empirically testable (Merton 1949). Similar themes

of understanding the influence of contextual variables recur across social science: Yarkoni (2022)

discusses the need to measure “stimuli, task, [and] instructions;” Bareinboim and Pearl (2013) call such

variables the “difference-generating factors.” Manzi (2012) describes the world as being “causally dense,”

with many potential contextual factors influencing a given phenomenon. Most directly, our research

builds on recent work by Almaatouq et al. (2022) and Levinthal and Rosenkopf (2020), who propose

quantifying a study’s defining attributes in its latent design space. Similarly, Simons, Shoda, and Lindsay


(2017) advocate for publishing statements of Constraints on Generality (COG) that explicitly identify the

context for which findings are expected to apply. Listing one’s design decisions and the implications they

may have on generalizability can distinguish a bounded “middle range” theory from a replication failure.

We directly apply these proposals to the domain of tasks, where we have demonstrated our method using

our labeled repository of tasks (the Task Map). If the impact of having a larger team depends on whether

the task involves a correct answer, the Task Map can coherently encode this idea alongside other possible

moderators. This integrative potential makes the Task Map useful for enhancing meta-analysis and

systematic review, which have been criticized for aggregating studies that are not “remotely comparable”

(Eysenck 1994). Finally, examining a study’s underlying dimensions may also inspire more

context-specific, or “solution-oriented,” research (Watts 2017). Managers working in different domains

may justifiably wonder whether a case study from another industry would apply to their own work.

Describing studies in terms of their underlying dimensions—and isolating the ones that are the key

“drivers” of an effect—would help practitioners identify which research studies and insights are most

relevant to them. The Task Space can therefore connect theory to practice, creating theory not for theory’s

sake, but for producing actionable, context-sensitive insights.

5.3. Commensurability Across Versions of the Task Space

Although our Task Space captures many key aspects of group tasks, it is not intended to be

comprehensive or even final. Rather, our contribution should be viewed as the first step in an iterative

process of Task Space construction and empirical validation as appropriate to the research domain of

interest—including removing uninformative dimensions, refining feature measurements, or

disaggregating individual constructs (e.g., “Creativity” could be further decomposed into its cognitive or

procedural components). We hope that unexpected findings will guide the modification of existing

dimensions or suggest new ones, allowing the framework to evolve.

A possible concern with this philosophy is that it will create many different “versions” of the Task Space,

which could undermine the stated goal of creating commensurability. If one researcher uses Task Space

1.0 and another uses Task Space 2.0, are we no better off than when we began—fragmented by

incompatible task descriptions and frameworks that cannot “speak to one another?”

While the need to narrow down to a relevant set of attributes is inevitable—it is impossible, in a “causally

dense” world, to account for every conceivable variable—incompatibility is not. The Task Space, at its

most fundamental level, is a way of thinking about tasks, presenting them not as discrete “types,” but as

points within a multidimensional space. Whereas categorical systems imply interdependencies between


dimensions (for example, “Creative” tasks are implicitly not “Intellective;” a “Maximizing” task is

implicitly not “Optimizing”), multidimensional spaces make minimal assumptions. Consequently, it is

easier to update a multidimensional space, because adding a new dimension does not require redefining

relationships between the existing categories. Different ways of thinking about tasks can be combined by

simply taking the union; and even when researchers select different subsets of task dimensions, we find in

a robustness check that key relationships between tasks are generally preserved (Appendix I2).

5.4. Limitations and Future Directions

Although we have already shown that the Task Space, as presented, is a useful device for reconciling

findings in the group and teams literature, we emphasize that this first step is associated with several key

limitations. For example, we chose a human annotation-based method of quantifying task dimensions, on

the grounds that it captures the impressions of task attributes from the perspective of a general population;

however, the multidimensional approach we propose is agnostic to the method of measurement. Future

researchers can introduce new methods, including expert annotations, Elo-style head-to-head

comparisons, and large language model-based annotation (see Gilardi, Alizadeh, and Kubli 2023).

Ultimately, many of the constructs in the Task Space are subjective (for example, what qualifies as a

“conflicting tradeoff” may be up to interpretation), and we expect that methods for measuring task

dimensions will be refined over time. If alternative measurements prove better at out-of-sample prediction

than the existing human annotations, the corresponding columns can be assigned greater weight and

redundant columns can be down-weighted or removed.

Beyond pure measurement issues, we acknowledge that tasks are still far more complex than we have

allowed in our 24-dimensional representation. As discussed in Section 3, our choice of focusing on the

task class means that the current Task Space considers only general attributes of a task’s stimuli and goals.

Dimensions outside of this scope include problem-solving strategies (e.g., Steiner (1972)’s _conjunctive_ ,

_disjunctive_ , and _discretionary_ tasks), typical participant behaviors (Roby and Lanzetta 1958), participants’

perceptions of the task (Shaw 1963 , Tushman 1979), and instance-level specifics (complexity, technology

affordances, incentive structures, and environmental factors). Each of these dimensions constitute design

spaces in their own right. For example, participant behaviors—termed the “group process”—are

well-studied (Barrick et al. 1998 , Oldeweme, Konradt, and Brede 2021 , Li et al. 2018), with extensive

reviews of subtopics, such as leadership (Carton 2022), as well as taxonomies on the subject (e.g., Marks,

Mathieu, and Zaccaro 2001). Similarly, group composition is another extensively researched field (Bell

2007 , Mathieu et al. 2014). Incorporating these richer conceptions of tasks (i.e., beyond the stimulus and

goals) will entail considerable additional work. Nonetheless, we see our approach—of “mapping” tasks in


relation to one another and quantifying the design space of an empirical question—as a proof of concept

that can be extended to other aspects of tasks, and even to other domains. That is, the procedure we have

outlined of quantifying and measuring the underlying variables in a domain is easily extensible to far

more general spaces; analogous to the Task Space that we have described here, one could also create a

Process Space, Composition Space, and so on.

Another line of future work will be extending the Task Space to field research. Whereas laboratory tasks

are short, self-contained, and can be completed by generalists with minimal training, these properties

rarely hold for tasks performed in an organizational context. In the field, members of teams must respond

to an ever-changing environment (“rugged fitness landscapes,” Levinthal 1997 ) and perform specialized

tasks embedded within long-term projects. Thus, the notion of a “task” will need to be redefined—a

process that we caution will not be trivial. Among the most significant changes will be to shift the focus

from class-level attributes to instance-level attributes, as well as to emphasize specialized skills. For

example, O*NET (originally introduced by Peterson et al. 2001), describes a “Sales Manager” in terms of

activities such as “Selling and Influencing Others” and “Establishing and Maintaining Interpersonal

Relationships.” Driskell, Salas, and Hogan (1987)’s analysis of military teams includes skill-oriented task

types such as “Mechanical/Technical,” “Manipulative/Persuasive,” and “Logical/Precision.” Wildman et

al. (2012) include features such as “Managing Others,” “Advising Others,” and “Human Service.” As

with the laboratory tasks we included in this work, there exist a myriad of ways to describe skill- and

role-related features, and we anticipate that building a multidimensional space of tasks for the field will

involve developing a shared language for describing work activities, then integrating relevant features

from across these frameworks.

More broadly, the integrative approach that inspires our work “naturally emphasizes contingencies and

enables practitioners to distinguish between the most general result and the result that is most useful in

practice” (Almaatouq, Griffiths, et al. 2024a). Rather than assume that a finding from a single case study

extends to teams in any context, the Task Space adopts the paradigm that one should first delineate a

study’s fundamental features. By forming and testing theories about these features, teams working in

organizations can create practices that survive rugged terrain.

**6. Conclusion**

Writing in 1966, Charles Morris argued for “a systematic map of the effects of different task

characteristics on various aspects of the group-interaction process.” But in the decades since his writing,

such a map was never created, despite many calls to better understand task features and how they impact

social science theories (Fleishman 1975 , Wood 1986 , Larson 2010 ). More recently, scholars have also


advocated for shifting from using categorical representations to using multidimensional methods of

measuring team constructs (Larson 2010 , Almaatouq et al. 2022 , Hollenbeck, Beersma, and Schouten

2012 , Lee et al. 2015 ). The Task Space (and its labeled repository, the Task Map) answers these calls,

creating, in effect, a “coordinate system” for team tasks that allows researchers to “navigate” between

existing tasks as if on a “map,” systematically visit as-yet unexplored tasks, and draw boundaries for

theories based on the “landscape” of task features. Our multidimensional representation of tasks enables

researchers to determine the extent to which an observed effect is generalizable, and it provides a key

piece of infrastructure to design studies, contextualize findings, and generate theoretical contingencies.

**7. Acknowledgements**

The authors thank the Alfred P. Sloan Foundation (Grant #202-13924) and the MIT Wade Fund for their

generous support of this research. We also thank the members of the Penn Computational Social Science

Lab’s Advisory Committee: Eytan Bakshy, Eric Bradlow, Colin Camerer, Angela Duckworth, James

Larson, Jim Manzi, Brian Uzzi, Ming Yin, and the late Daniel Kahneman. We also thank our research

assistants, Daria Paniukhina, Joyce An-Jie Wang, Sarika Subramanian, Karan Sampath, Dodge Hill, and

Vikram Balasubramanian, all of whom were instrumental in the literature review and task extraction

process. We thank Matthew Cronin, Mohammed Alsobay, Michael Cooper, James Houghton, Michelle

Vaccaro, and Robin Na for their feedback.

**References**

Aggarwal, Ishani, and Anita Williams Wooley. 2019. “Team Creativity, Cognition, and Cognitive Style
Diversity.” _Management Science_ 65 (4): 1586–99.
Allport, Gordon W., and Henry S. Odbert. 1936. “Trait-Names: A Psycho-Lexical Study.” _Psychological
Monographs_ 47 (1).
Almaatouq, Abdullah, Mohammed Alsobay, Ming Yin, and Duncan J. Watts. 2021. “Task Complexity
Moderates Group Synergy.” _Proceedings of the National Academy of Sciences_ 118 (36):
e2101062118. https://doi.org/10.1073/pnas.2101062118.
Almaatouq, Abdullah, Mohammed Alsobay, Ming Yin, and Duncan J. Watts. 2024. “The Effects of Group
Composition and Dynamics on Collective Performance.” _Topics in Cognitive Science_ 16 (2):
302–21. https://doi.org/10.1111/tops.12706.
Almaatouq, Abdullah, Joshua Becker, James P. Houghton, Nicolas Paton, Duncan J. Watts, and Mark E.
Whiting. 2021. “Empirica: A Virtual Lab for High-Throughput Macro-Level Experiments.”
_Behavior Research Methods_ 53 (5): 2158–71. https://doi.org/10.3758/s13428-020-01535-9.
Almaatouq, Abdullah, Thomas L Griffiths, Jordan W Suchow, Mark E Whiting, James Evans, and
Duncan J Watts. 2024a. “Beyond Playing 20 Questions with Nature: Integrative Experiment
Design in the Social and Behavioral Sciences.” _Brain and Behavioral Sciences_ 47: 1–55.
Almaatouq, Abdullah, Thomas L Griffiths, Jordan W Suchow, Mark E Whiting, James Evans, and
Duncan J Watts. 2024b. “Replies to Commentaries on Beyond Playing 20 Questions with
Nature.” _Brain and Behavioral Sciences_ 47 (e65). https://doi.org/10.1017/S0140525X23002789.
Almaatouq, Abdullah, Alejandro Noriega-Campero, Abdulrahman Alotaibi, P. M. Krafft, Mehdi


Moussaid, and Alex Pentland. 2020. “Adaptive Social Networks Promote the Wisdom of
Crowds.” _Proceedings of the National Academy of Sciences_ 117 (21): 11379–86.
https://doi.org/10.1073/pnas.1917687117.
Almaatouq, Abdullah, M. Amin Rahimian, Jason W. Burton, and Abdulla Alhajri. 2022. “The
Distribution of Initial Estimates Moderates the Effect of Social Influence on the Wisdom of the
Crowd.” _Scientific Reports_ 12 (1). https://doi.org/10.1038/s41598-022-20551-7.
Altmann, André, Laura Toloşi, Oliver Sander, and Thomas Lengauer. 2010. “Permutation Importance: A
Corrected Feature Importance Measure.” _Bioinformatics_ 26 (10): 1340–47.
https://doi.org/10.1093/bioinformatics/btq134.
Arrow, Kenneth J., Robert Forsythe, Michael Gorham, et al. 2008. “The Promise of Prediction Markets.”
_Science_ 320 (5878): 877–78. https://doi.org/10.1126/science.1157679.
Asch, Solomon. 1956. “Studies of Independence and Conformity: I. A Minority of One against a
Unanimous Majority.” _Psychological Monographs: General and Applied_ 70 (9): 1–70.
Bahrami, Bahador, Karsten Olsen, Peter E. Latham, Andreas Roepstorff, Geraint Rees, and Chris D. Frith.

2010. “Optimally Interacting Minds.” _Science_ 329 (5995): 1081–85.
https://doi.org/10.1126/science.1185718.
Bailey, Kenneth D. 1989. “Taxonomies and Disaster: Prospects and Problems.” _International Journal of
Mass Emergencies and Disasters_ 7 (3): 419–31.
Bailey, Kenneth D. 1994. “Typologies and Taxonomies in Social Science.” In _Typologies and Taxonomies_.
SAGE Publications, Inc. https://doi.org/10.4135/9781412986397.n1.
Balietti, Stefano, Brennan Klein, and Christoph Riedl. 2021. “Optimal Design of Experiments to Identify
Latent Behavioral Types.” _Experimental Economics_ 24 (3): 772–99.
https://doi.org/10.1007/s10683-020-09680-w.
Bareinboim, Elias, and Judea Pearl. 2013. “A General Algorithm for Deciding Transportability of
Experimental Results.” _Journal of Causal Inference_ 1 (1): 107–34.
https://doi.org/10.1515/jci-2012-0004.
Baribault, Beth, Chris Donkin, Daniel R. Little, et al. 2018. “Metastudies for Robust Tests of Theory.”
_Proceedings of the National Academy of Sciences_ 115 (11): 2607–12.
https://doi.org/10.1073/pnas.1708285114.
Baron, Jonathan, and John C Hershey. 1988. “Outcome Bias in Decision Evaluation.” _Journal of
Personality and Social Psychology_ 54 (4): 569–79.
Barrick, Murray R., Bret H. Bradley, Amy L. Kristof-Brown, and Amy E. Colbert. 2007. “The
Moderating Role of Top Management Team Interdependence: Implications for Real Teams and
Working Groups.” _Academy of Management Journal_ 50 (3): 544–57.
https://doi.org/10.5465/amj.2007.25525781.
Barrick, Murray R., Greg L. Stewart, Mitchell J. Neubert, and Michael K. Mount. 1998. “Relating
Member Ability and Personality to Work-Team Processes and Team Effectiveness.” _Journal of
Applied Psychology_ 83 (3): 377. https://doi.org/10.1037/0021-9010.83.3.377.
Batista, Rafael M, and James Ross. 2024. “Words That Work: Using Language to Generate Hypotheses.”
Preprint.
Bavelas, Alex. 1950. “Communication Patterns in Task-Oriented Groups.” _The Journal of the Acoustical
Society of America_ 22 (August): 725–30.
Becker, Joshua, Abdullah Almaatouq, and Emőke-Ágnes Horvát. 2021. “Network Structures of Collective
Intelligence: The Contingent Benefits of Group Discussion.” arXiv:2009.07202. Preprint, arXiv,
March 8. [http://arxiv.org/abs/2009.07202.](http://arxiv.org/abs/2009.07202.)
Bell, Suzanne T. 2007. “Deep-Level Composition Variables as Predictors of Team Performance: A
Meta-Analysis.” _Journal of Applied Psychology_ 92 (3): 595.
https://doi.org/10.1037/0021-9010.92.3.595.
Brunswik, Egon. 1956. “Representative Design and Probabilistic Theory in a Functional Psychology.”
_Psychological Review_ 62 (3): 193. https://doi.org/10.1037/h0047470.


Camerer, Colin F. 1997. “Progress in Behavioral Game Theory.” _Journal of Economic Perspectives_ 11
(4): 167–88. https://doi.org/10.1257/jep.11.4.167.
Carton, Andrew M. 2022. “The Science of Leadership: A Theoretical Model and Research Agenda.”
_Annual Review of Organizational Psychology and Organizational Behavior_ 9 (1): 61–93.
https://doi.org/10.1146/annurev-orgpsych-012420-091227.
Chang, Edward H., Erika L. Kirgios, and Rosanna K. Smith. 2021. “Large-Scale Field Experiment Shows
Null Effects of Team Demographic Diversity on Outsiders’ Willingness to Support the Team.”
_Journal of Experimental Social Psychology_ 94 (May): 104099.
https://doi.org/10.1016/j.jesp.2020.104099.
Chen, Weiyun, and Xin Li. 2012. “Deciphering Wisdom of Crowds from Their Influenced Binary
Decisions.” _2012 IEEE International Conference on Intelligence and Security Informatics_ , June,
235–40. https://doi.org/10.1109/ISI.2012.6284316.
Chen, Yiling, Chao-Hsien Chu, Tracy Mullen, and David M Pennock. 2005. “Information Markets vs.
Opinion Pools: An Empirical Comparison.” _EC’05, Vancouver, British Columbia, Canada_ , June
5.
Cohen, Susan G., and Diane E. Bailey. 1997. “What Makes Teams Work: Group Effectiveness Research
from the Shop Floor to the Executive Suite.” _Journal of Management_ 23 (3): 239–90.
https://doi.org/10.1177/014920639702300303.
De Dreu, Carsten K. W., and Laurie R. Weingart. 2003. “Task versus Relationship Conflict, Team
Performance, and Team Member Satisfaction: A Meta-Analysis.” _Journal of Applied Psychology_
88 (4): 741–49. https://doi.org/10.1037/0021-9010.88.4.741.
Dhami, Mandeep K., Ralph Hertwig, and Ulrich Hoffrage. 2004. “The Role of Representative Design in
an Ecological Approach to Cognition.” _Psychological Bulletin_ 130 (6): 959.
https://doi.org/10.1037/0033-2909.130.6.959.
Diehl, Michael, and Wolfgang Stroebe. 1987. “Productivity Loss in Brainstorming Groups: Toward the
Solution of a Riddle.” _Journal of Personality and Social Psychology_ (US) 53 (3): 497–509.
https://doi.org/10.1037/0022-3514.53.3.497.
Driskell, James E, Eduardo Salas, and Robert Hogan. 1987. _A Taxonomy for Composing Effective Naval
Teams_. Naval Training Systems Center.
Epley, Nicholas, and Thomas Gilovich. 2006. “The Anchoring-and-Adjustment Heuristic: Why the
Adjustments Are Insufficient.” _Psychological Science_ 17 (4): 311–18.
https://doi.org/10.1111/j.1467-9280.2006.01704.x.
Ericksen, Jeff, and Lee Dyer. 2004. “Right from the Start: Exploring the Effects of Early Team Events on
Subsequent Project Team Development and Performance.” _Administrative Science Quarterly_ 49
(3): 438–71. https://doi.org/10.2307/4131442.
Eyke, Natalie S., William H. Green, and Klavs F. Jensen. 2020. “Iterative Experimental Design Based on
Active Machine Learning Reduces the Experimental Burden Associated with Reaction
Screening.” _Reaction Chemistry & Engineering_ 5 (10): 1963–72.
https://doi.org/10.1039/D0RE00232A.
Eysenck, H. J. 1994. “Systematic Reviews: Meta-Analysis and Its Problems.” Education and Debate. _BMJ_
309 (6957): 789–92. https://doi.org/10.1136/bmj.309.6957.789.
Fleishman, Edwin A. 1975. “Toward a Taxonomy of Human Performance.” _American Psychologist_ ,
December, 23.
Gilardi, Fabrizio, Meysam Alizadeh, and Maël Kubli. 2023. “ChatGPT Outperforms Crowd-Workers for
Text-Annotation Tasks.” arXiv:2303.15056. Preprint, arXiv, March 27.
[http://arxiv.org/abs/2303.15056.](http://arxiv.org/abs/2303.15056.)
Goldberg, Lewis R. 1993. “The Structure of Phenotypic Personality Traits.” _American Psychologist_.
Goodwin, Gerald F., Nikki Blacksmith, and Meredith R. Coats. 2018. “The Science of Teams in the
Military: Contributions from over 60 Years of Research.” _American Psychologist_ 73 (4): 322–33.
https://doi.org/10.1037/amp0000259.


Gross, Edward. 1954. “Primary Functions of the Small Group.” _American Journal of Sociology_ 60 (1):
24–29.
Gully, Stanley M., Kara A. Incalcaterra, Aparna Joshi, and J. Matthew Beaubien. 2002. “A Meta-Analysis
of Team-Efficacy, Potency, and Performance: Interdependence and Level of Analysis as
Moderators of Observed Relationships.” _Journal of Applied Psychology_ 87 (5): 819.
https://doi.org/10.1037/0021-9010.87.5.819.
Hackman, J Richard. 1968a. _Towards Understanding the Role of Tasks in Behavioral Research_. Scientific
Interim Report. Department of Administrative Sciences, Yale University.
Hackman, J Richard. 1968b. “Effects of Task Characteristics on Group Products.” _Journal of
Experimental Social Psychology_ 4 (2): 28.
Hackman, J. Richard, and Greg R. Oldham. 1975. “Development of the Job Diagnostic Survey.” _Journal
of Applied Psychology_ 60 (2): 159. https://doi.org/10.1037/h0076546.
Harris, Alexa M., Diego Gómez-Zará, Leslie A. DeChurch, and Noshir S. Contractor. 2019. “Joining
Together Online: The Trajectory of CSCW Scholarship on Group Formation.” _Proceedings of the
ACM on Human-Computer Interaction_ 3 (CSCW): 1–27. https://doi.org/10.1145/3359250.
Herold, David M. 1978. “Improving the Performance Effectiveness of Groups Through a Task-Contingent
Selection of Intervention Strategies.” _The Academy of Management Review_ 3 (2).
Hill, Gayle W. 1982. “Group versus Individual Performance: Are <em>N</Em> + 1 Heads Better than
One?” _Psychological Bulletin_ 91 (3): 517. https://doi.org/10.1037/0033-2909.91.3.517.
Hollenbeck, John R., Bianca Beersma, and Maartje E. Schouten. 2012. “Beyond Team Types and
Taxonomies: A Dimensional Scaling Conceptualization for Team Description.” _Academy of
Management Review_ 37 (1): 82–106. https://doi.org/10.5465/amr.2010.0181.
Hough, Leatta M. 1992. “The ‘Big Five’ Personality Variables — Construct Confusion: Description
Versus Prediction.” _Human Performance_ 5 (1 & 2): 139–55.
Hueffmeier, Joachim, and Guido Hertel. 2011. “When the Whole Is More than the Sum of Its Parts:
Group Motivation Gains in the Wild.” _JOURNAL OF EXPERIMENTAL SOCIAL PSYCHOLOGY_
(San Diego) 47 (2): 455–59. https://doi.org/10.1016/j.jesp.2010.12.004.
Husband, Richard Wellington. 1940. “Cooperative versus Solitary Problem Solution: The Journal of
Social Psychology: Vol 11, No 2.” _The Journal of Social Psychology_ 11 (2).
https://www.tandfonline.com/doi/abs/10.1080/00224545.1940.9918759.
Janis, Ivring L. 1971. “Groupthink.” _Psychology Today_.
Koriat, Asher. 2012. “When Are Two Heads Better than One and Why?” _Science_ 336 (6079): 360–62.
https://doi.org/10.1126/science.1216549.
Krackhardt, David, and Robert N. Stern. 1988. “Informal Networks and Organizational Crises: An
Experimental Simulation.” _Social Psychology Quarterly_ 51 (2): 123–40.
Larson, James R. 2010. _In Search of Synergy in Small Group Performance_. Psychology Press.
Laughlin, Patrick R, and Alan L Ellis. 1986. “Demonstrability and Social Combination Processes on
Mathematical Intellective Tasks.” _Journal of Experimental Social Psychology_ 22: 177–98.
Laughlin, Patrick R., Erin C. Hatch, Jonathan S. Silver, and Lee Boh. 2006. “Groups Perform Better than
the Best Individuals on Letters-to-Numbers Problems: Effects of Group Size.” _Journal of
Personality and Social Psychology_ (US) 90 (4): 644–51.
https://doi.org/10.1037/0022-3514.90.4.644.
Laughlin, Patrick R., Norbert L. Kerr, James H. Davis, Henry M. Halff, and Kenneth A. Marciniak. 1975.
“Group Size, Member Ability, and Social Decision Schemes on an Intellective Task.” _Journal of
Personality and Social Psychology_ 31 (3): 522–35. https://doi.org/10.1037/h0076474.
Lee, Stephanie M., Joel Koopman, John R. Hollenbeck, Linda C. Wang, and Klodiana Lanaj. 2015. “The
Team Descriptive Index (TDI): A Multidimensional Scaling Approach for Team Description.”
_Academy of Management Discoveries_ 1 (1): 91–116. https://doi.org/10.5465/amd.2013.0001.
Levinthal, Daniel A. 1997. “Adaptation on Rugged Landscapes.” _Management Science_ 43 (7): 934–50.
Levinthal, Daniel A, and Lori Rosenkopf. 2020. _Commensurability and Collective Impact in Strategic_


_Management Research_. November 14, 35.
Li, Guiquan, Alex L. Rubenstein, Weipeng Lin, Mo Wang, and Xingwen Chen. 2018. “The Curvilinear
Effect of Benevolent Leadership on Team Performance: The Mediating Role of Team Action
Processes and the Moderating Role of Team Commitment.” _Personnel Psychology_ 71 (3):
369–97. https://doi.org/10.1111/peps.12264.
Lorge, Irving, and Herbert Solomon. 1960. “Group and Individual Performance in Problem Solving
Related to Previous Exposure to Problem, Level of Aspiration, and Group Size.” _Behavioral
Science_ 5 (1): 28–38. https://doi.org/10.1002/bs.3830050103.
Lundberg, Scott M, and Su-In Lee. 2017. “A Unified Approach to Interpreting Model Predictions.”
_Advances in Neural Information Processing Systems_ 30.
https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.h
tml.
Manzi, Jim. 2012. _Uncontrolled: The Surprising Payoff of Trial-and-Error for Business, Politics, and
Society_. Basic Books.
Mao, Andrew, Winter Mason, Siddharth Suri, and Duncan J. Watts. 2016. “An Experimental Study of
Team Size and Performance on a Complex Task.” _PLOS ONE_ 11 (4): e0153048.
https://doi.org/10.1371/journal.pone.0153048.
Marks, Michelle A, John E Mathieu, and Stephen I Zaccaro. 2001. “A Temporally Based Framework and
Taxonomy of Team Processes.” _Academy of Management Review_ 26 (3): 356–76.
Marquart, Dorothy Irene. 1955. “Group Problem Solving.” _The Journal of Social Psychology_ 41 (1):
103–13. world.
Mason, Winter, and Duncan J. Watts. 2011. “Collaborative Learning in Networks.” _Proceedings of the
National Academy of Sciences_ 109 (3): 764–69. https://doi.org/10.1073/pnas.1110069108.
Mathieu, John E., John R. Hollenbeck, Daan van Knippenberg, and Daniel R. Ilgen. 2017. “A Century of
Work Teams in the Journal of Applied Psychology.” _Journal of Applied Psychology_ 102 (3): 452.
https://doi.org/10.1037/apl0000128.
Mathieu, John E., Scott I. Tannenbaum, Jamie S. Donsbach, and George M. Alliger. 2014. “A Review and
Integration of Team Composition Models: Moving Toward a Dynamic and Temporal
Framework.” _Journal of Management_ 40 (1): 130–60.
https://doi.org/10.1177/0149206313503014.
McCormick, Ernest J., Paul R. Jeanneret, and Robert C. Mecham. 1972. “A Study of Job Characteristics
and Job Dimensions as Based on the Position Analysis Questionnaire (PAQ).” _Journal of Applied
Psychology_ 56 (4): 347–68. https://doi.org/10.1037/h0033099.
McGrath, Joseph E. 1984. _Groups: Interaction and Performance_. Prentice-Hall, Inc.
Meluso, John, and Laurent Hébert-Dufresne. 2023. “Multidisciplinary Learning through Collective
Performance Favors Decentralization.” _Proceedings of the National Academy of Sciences_ 120
(34): e2303568120. https://doi.org/10.1073/pnas.2303568120.
Merton, Robert K. 1949. “On Sociological Theories of the Middle Range.” In _Classical Sociological
Theory_ , 2nd ed., edited by Craig J. Calhoun. Blackwell Pub.
[http://www.csun.edu/~snk1966/Robert%20K%20Merton%20-%20On%20Sociological%20Theor](http://www.csun.edu/~snk1966/Robert%20K%20Merton%20-%20On%20Sociological%20Theor)
ies%20of%20the%20Middle%20Range.pdf.
Meslec, Nicoleta, Petru Lucian Curseu, Marius T. H. Meeus, and Oana C. Iederan Fodor. 2014. “When
None of Us Perform Better than All of Us Together: The Role of Analogical Decision Rules in
Groups.” _PLoS ONE_ (San Francisco) 9 (1): e85232.
https://doi.org/10.1371/journal.pone.0085232.
Morris, Charles G. 1966. “Task Effects on Group Interaction.” _Journal of Personality and Social
Psychology_ 4 (5): 545–54.
Mullen, Brian, Craig Johnson, and Eduardo Salas. 1991. “Productivity Loss in Brainstorming Groups: A
Meta-Analytic Integration.” _Basic and Applied Social Psychology_ 12 (1): 3–23.
https://doi.org/10.1207/s15324834basp1201_1.


Oldeweme, Martina, Udo Konradt, and Max Brede. 2021. “The Rhythm of Teamwork: Discovering a
Complex Temporal Pattern of Team Processes.” _Group Dynamics: Theory, Research, and
Practice_ 27 (1): 50. https://doi.org/10.1037/gdn0000175.
Peterson, Norman G., Michael D. Mumford, Walter C. Borman, et al. 2001. “Understanding Work Using
the Occupational Information Network (O*NET): Implications for Practice and Research.”
_Personnel Psychology_ 54 (2): 451–92. https://doi.org/10.1111/j.1744-6570.2001.tb00100.x.
Peterson, Randall S, Pamela D Owens, Philip E Tetlock, and Elliott T Fan. 1998. “Group Dynamics in
Top Management Teams: Groupthink, Vigilance, and Alternative Models of Organizational
Failure and Success.” _Organizational Behavior and Human Decision Processes_ 73 (2/3):
272–305.
Riedl, Christoph, Young Ji Kim, Pranav Gupta, Thomas W. Malone, and Anita Williams Woolley. 2021.
“Quantifying Collective Intelligence in Human Groups.” _Proceedings of the National Academy of
Sciences_ 118 (21): e2005737118. https://doi.org/10.1073/pnas.2005737118.
Roby, Thornton B., and John T. Lanzetta. 1958. “Considerations in the Analysis of Group Tasks.”
_Psychological Bulletin_ 55 (2): 88–101. https://doi.org/10.1037/h0047233.
Salas, Eduardo, Denise L. Reyes, and Susan H. McDaniel. 2018. “The Science of Teamwork: Progress,
Reflections, and the Road Ahead.” _American Psychologist_ 73 (4): 593–600.
https://doi.org/10.1037/amp0000334.
Shaw, Marvin E. 1963. “Scaling Group Tasks: A Method for Dimensional Analysis: (532082008-001).”
American Psychological Association. https://doi.org/10.1037/e532082008-001.
Shore, Jesse, Ethan Bernstein, and David Lazer. 2015. “Facts and Figuring: An Experimental
Investigation of Network Structure and Performance in Information and Solution Spaces.”
_Organization Science_ 26 (5): 1432–46. https://doi.org/10.1287/orsc.2015.0980.
Silver, Ike, Barbara A. Mellers, and Philip E. Tetlock. 2021. “Wise Teamwork: Collective Confidence
Calibration Predicts the Effectiveness of Group Discussion.” _Journal of Experimental Social
Psychology_ 96 (September): 104157. https://doi.org/10.1016/j.jesp.2021.104157.
Simons, Daniel J., Yuichi Shoda, and D. Stephen Lindsay. 2017. “Constraints on Generality (COG): A
Proposed Addition to All Empirical Papers.” _Perspectives on Psychological Science_ 12 (6):
1123–28. https://doi.org/10.1177/1745691617708630.
Simonsohn, Uri, Andres Montealegre, and Ioannis Evangelidis. 2024. “Stimulus Sampling Reimagined:
Designing Experiments with Mix-and-Match, Analyzing Results with Stimulus Plots.” _SSRN
Electronic Journal_ , ahead of print. https://doi.org/10.2139/ssrn.4716832.
Stasser, Garold, and William Titus. 1985. “Pooling of Unshared Information in Group Decision Making:
Biased Information Sampling During Discussion.” _Journal of Personality and Social Psychology_
48 (5): 1467–78.
Stasson, Mark F., and Scott D. Bradshaw. 1995. “Explanations of Individual-Group Performance
Differences: What Sort of ‘Bonus’ Can Be Gained Through Group Interaction?” _Small Group
Research_ 26 (2): 296–308. https://doi.org/10.1177/1046496495262007.
Steiner, Ivan D. 1972. _Group Process and Productivity_. Academic Press.
Stewart, Greg L., and Murray R. Barrick. 2000. “Team Structure and Performance: Assessing the
Mediating Role of Intrateam Process and the Moderating Role of Task Type.” _Academy of
Management Journal_ 43 (2): 135–48.
Straub, Vincent J, Milena Tsvetkova, and Taha Yasseri. 2023. “The Cost of Coordination Can Exceed the
Benefit of Collaboration in Performing Complex Tasks.” _Collective Intelligence_ 2 (2):

263391372311569. https://doi.org/10.1177/26339137231156912.
Thompson, Leigh L., and Elizabeth Ruth Wilson. 2015. “Creativity in Teams.” In _Emerging Trends in the
Social and Behavioral Sciences: An Interdisciplinary, Searchable, and Linkable Resource_. John
Wiley & Sons. 10.1002/9781118900772.etrds0056.
Thompson, William R. 1933. “On the Likelihood That One Unknown Probability Exceeds Another in
View of the Evidence of Two Samples.” _Biometrika_ 25 (3–4): 285–94.


https://doi.org/10.1093/biomet/25.3-4.285.
Tushman, Michael L. 1979. “Work Characteristics and Subunit Communication Structure: A Contingency
Analysis.” _Administrative Science Quarterly_ 24 (1): 82–98. https://doi.org/10.2307/2989877.
Valentine, Melissa A., Ingrid M. Nembhard, and Amy C. Edmondson. 2015. “Measuring Teamwork in
Health Care Settings: A Review of Survey Instruments.” _Medical Care_ 53 (4): e16–30.
Watts, Duncan J. 2017. “Should Social Science Be More Solution-Oriented?” _Nature Human Behaviour_ 1
(1): 0015. https://doi.org/10.1038/s41562-016-0015.
Weber, Bernhard, and Guido Hertel. 2007. “Motivation Gains of Inferior Group Members: A
Meta-Analytical Review.” _Journal of Personality and Social Psychology_ 93 (6): 973–93.
https://doi.org/10.1037/0022-3514.93.6.973.
Weidmann, Ben, and David J. Deming. 2021. “Team Players: How Social Skills Improve Team
Performance.” _Econometrica_ 89 (6): 2637–57. https://doi.org/10.3982/ECTA18461.
Wells, Gary L., and Paul D. Windschitl. 1999. “Stimulus Sampling and Social Psychological
Experimentation.” _Personality and Social Psychology Bulletin_ 25 (9): 1115–25.
https://doi.org/10.1177/01461672992512005.
Whiting, Mark E., Allie Blaising, Chloe Barreau, et al. 2019. “Did It Have To End This Way?:
Understanding The Consistency of Team Fracture.” _Proceedings of the ACM on
Human-Computer Interaction_ 3 (CSCW): 1–23. https://doi.org/10.1145/3359311.
Wildman, Jessica L., Amanda L. Thayer, Michael A. Rosen, Eduardo Salas, John E. Mathieu, and Sara R.
Rayne. 2012. “Task Types and Team-Level Attributes: Synthesis of Team Classification
Literature.” _Human Resource Development Review_ 11 (1): 97–129.
https://doi.org/10.1177/1534484311417561.
Wood, Robert E. 1986. “Task Complexity: Definition of the Construct.” _Organizational Behavior and
Human Decision Processes_ 37 (1): 60–82. https://doi.org/10.1016/0749-5978(86)90044-0.
Woolley, Anita Williams, Christopher F. Chabris, Alex Pentland, Nada Hashmi, and Thomas W. Malone.

2010. “Evidence for a Collective Intelligence Factor in the Performance of Human Groups.”
_Science_ 330 (6004): 686–88. https://doi.org/10.1126/science.1193147.
Yarkoni, Tal. 2022. “The Generalizability Crisis.” _Behavioral and Brain Sciences_ 45: e1.
https://doi.org/10.1017/S0140525X20001685.
Zigurs, Ilze, Bonnie K. Buckland, James R. Connolly, and E. Vance Wilson. 1999. “A Test of
Task-Technology Fit Theory for Group Support Systems.” _ACM SIGMIS Database: The
DATABASE for Advances in Information Systems_ 30 (3–4): 34–50.
https://doi.org/10.1145/344241.344244.


