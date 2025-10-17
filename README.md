# GFQL

## What is GFQL?

GFQL (Graph dataFrame Query Language) is an open-source embeddable graph query language for data scientists, analysts, and developers working with graph data. It combines the expressiveness of graph analytics with the performance of modern dataframe operations, enabling native in-memory large-scale columnar computing on graph structures. GFQL makes it easy to wrangle, transform, and analyze graph data using familiar dataframe-style operations while leveraging GPU acceleration for processing graphs with billions of edges.

**GFQL enables graph wrangling without requiring a graph database.** You can separate your storage tier (SQL databases, files, data lakes, or graph databases) from how your application or cluster handles graph operations like shaping, cleaning, pattern searching, algorithmic enrichments, and visualization. Work directly with your existing data infrastructure.

GFQL is trusted by banks, startups, security teams, and every Graphistry user for mission-critical graph analytics and investigation workflows.

## Top Features

- **Embeddable Graph Queries**: Write expressive graph traversals and pattern matching queries that can be embedded directly in your Python workflows
- **Dataframe-Native Operations**: Leverage familiar dataframe APIs (pandas, cuDF, Apache Arrow) for graph computations with seamless integration
- **GPU-Accelerated Performance**: Process massive graphs with billions of edges using GPU acceleration for unprecedented speed. Part of the NVIDIA Rapids ecosystem for high-performance GPU computing
- **Columnar Computing**: Efficient in-memory columnar storage and operations optimized for modern analytics workloads
- **Open Source & Extensible**: Fully open source with extensible architecture for custom graph operations and integrations
- **Rich Connector Ecosystem**: Seamlessly integrate with your existing data infrastructure without requiring a graph database:
  - **File Formats**: CSV, Parquet, Excel (XLSX), JSON
  - **Data Platforms & SQL**: Databricks, Splunk, PostgreSQL, Azure Data Explorer (Kusto), Google Cloud Spanner
  - **Graph Databases** (optional): Neo4j, Amazon Neptune, TigerGraph, ArangoDB, Memgraph
  - **Python Tools**: Pandas, Apache Arrow, NVIDIA RAPIDS cuDF, NetworkX, Graphviz

## Next Steps

- [GFQL Documentation](https://pygraphistry.readthedocs.io/en/latest/gfql/overview.html) - Complete guide in the PyGraphistry Read the Docs
- [PyGraphistry GitHub Repository](https://github.com/graphistry/pygraphistry) - Main project repository with GFQL implementation
- [2B Edge Graph GPU Result](https://www.linkedin.com/posts/graphistry_at-graph-the-planet-2025-we-showed-gfql-activity-7341259182924304385-F8XF?utm_source=share&utm_medium=member_android&rcm=ACoAAAPO5vIBimmdPlYKpPDVS8xKMWdcgjz403A) - 2025 LinkedIn post about GFQL's 2 billion edge graph GPU performance
- [What is Graph Intelligence?](https://gradientflow.com/what-is-graph-intelligence/) - 2022 article by Ben Lorica at Gradient Flow on graph intelligence in the compute tier
