# Duplicate Bug Report Detection with a Combination of Information Retrieval and Topic Modeling. Automated Software Engineering (ASE), 2012 Proceedings of the 27th IEEE/ACM International Conference. Anh Tuan Nguyen, Tung Thanh Nguyen, Tien N. Nguyen, David Lo, Chengnian Sun.

## Keywords:
#### Duplicate Bug Reports - If the technical issues in a system have been previously encountered as part of a bug report, then succeeding bug reports containing the description of the same issues is referred to as a duplicate bug report.

#### Topic Model - This model is used to detect duplicate bug reports even when they have textual dissimilarities. This kind of modelling is often used to discover semantic structure in a body of text.

#### Information Retrieval - This is concerned with obtaining information resources which are relevant from a collection of information resources.

## Motivation: 
Multiple people working on the same software project might often encounter the same technical issue. This will cause them to present these issues as bug reports, and describe the bug's misbehaviour in the context in which they encountered it. Therefore, duplicate reports are recognized as separate and independent issues, which leads to redundant efforts in fixing it. Detection of duplicate reports, even those with textual differences, will make reduce the redundant efforts towards fixing the issue. Moreover, detection of duplicate reports will also enable us to view and analyze the issue from multiple perspectives, making it easier to fix.

## DBTM (Dupicate Bug Report Topic Model): 
DBTM is a combination of two things, T-Model, a novel topic model; and BM25F, which is an advanced document similarity function that uses weigthed word vectors of documents. The T-Model uses topic-based features to predict duplicate reports, while BM25F uses textual features.

## Evaluation:
The system was evaluated using datasets from Eclipse, OpenOffice, and Mozilla, while varying the number of topics (K) for each. For lower values of K (<60), the accuracy of prediction was low as the number of features were too small to distinguish technical functions. As K increases, the accuracy also increases and becomes stable after a while. The time taken to find these duplicate bug reports is linear to the size of the project, i.e. the total number of bug reports.

## Conclusion:
We can see that DBTM, trained with historical data, can find duplicate reports detailing the same issue but using different terms. The evaluation of real world systems shows an improvement in accuracy of detection of up to 20% compared to other state-of-the-art approaches.
