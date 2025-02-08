<h1 align="center">Why Polars?</h1>

Overview:
=================

<p align="justify">Performance Polars was developed with a focus on performance and efficiency, using parallel processing and vectorized operations. Polars uses an Arrow DataFrame (Apache Arrow) based model, which offers better performance due to its data structure optimized for vectorized and in-memory operations.</p>
<p align="justify">Memory Usage Polars is highly efficient in terms of memory usage, using less memory to store data, especially when working with large volumes of data.</p>
<p align="justify">"Lazy" API Polars supports a Lazy API, which means you can create a pipeline of transformations without actually executing them until a final result is requested. Lazy mode in Polars allows you to create an execution plan and, instead of calculating on the fly, Polars will optimize the sequence of transformations and perform the calculations more efficiently.</p>
<p align="justify">Native Parallelism Polars was designed from the ground up to take advantage of parallelism and distributed execution, which makes it much more efficient to execute operations on multiple cores.</p>
<p align="justify">Consistent and Concise API Polars has a more consistent API, especially when compared to the evolution of Pandas, which has introduced changes over time. Polars' API is closer to a functional approach.</p>
<p align="justify">Ease of Complex Data Types Polars has native support for data types such as Lists and Strings, making it easier to deal with more complex and hierarchical data types.</p>
<p align="justify">Compatibility with Apache Arrow Polars uses Apache Arrow as its in-memory data format. This makes it easier to integrate with other tools that also use Arrow, such as distributed storage systems and Big Data.</p>
<p align="justify">Integration with other tools Polars has simpler and more direct integration with PyArrow and other Arrow-based technologies.</p>
<p align="justify">Conclusion: Polars is ideal for when you deal with large volumes of data, need high performance, efficient use of memory, and want parallel execution.</p>


<h3>ETL with Polars</h3>
=================

<p align="justify">The ETL (Extract, Transform, Load) process can be done in 3 steps: extract the data from the CSV, transform it and then load it to AWS.</p>
<p align="justify">Step 1: Extract the data with Polars First, let's read the CSV file using the Polars library.</p>
<p align="justify">Step 2: Transform the data Now, let's apply some transformations to the dataframe.</p>
<p align="justify">Step 3: Load the data to AWS (S3) Now, let's load the data to Amazon S3, using boto3, which is the official AWS library to interact with its services.</p>
<p align="justify">Process Summary: We created a fictitious database in CSV. We use Polars to perform transformations on the dataframe, such as calculating age from date of birth. We upload the transformed data to AWS S3.</p>

<h3>ELT with Polars </h3>
=================

<p align="justify">Step 1: Load the data into AWS Athena.</p>
<p align="justify">Step 2: Transform the data with Polars Now that we have the data in Athena, the next step is to perform Transform using Polars. Let's connect to Athena and read the data using boto3 and PyAthena.</p>
<p align="justify">Step 3: Load the transformed data to S3 (Data Warehouse) Now that the data is transformed, we can load it back to S3 as a new CSV file, which will be used as a data warehouse.</p>
