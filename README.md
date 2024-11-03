<img width="745" alt="image" src="https://github.com/user-attachments/assets/ada7a529-2a8c-4427-88d0-35607dd2bf26">



Start: Intelligent Routing System
|
|--> **User Input Handling**
|    |
|    |--> Receive User Query
|    |--> Route Query to Primary Router
|    |--> Output: Selected Model Based on Query Type
|
|--> **Primary Routing Process**
|    |
|    |--> Check Query Type and Complexity
|         |
|         |-- Complex Query --> Model: Llama3-70b-versatile
|         |
|         |-- Code Query --> Model: Llama3-70b-8192
|         |
|         |-- Simple Conversation --> Model: Gemma-7b-it
|    |--> Output: Model Selected for Query
|
|--> **Secondary Routing Process (System Messages)**
|    |
|    |--> Route to Secondary Router Based on Model
|    |    |
|    |    |--> For Llama3-70b-versatile: Select System Message by Topic
|    |    |    |
|    |    |    |--> Options: Literature Expert, Scientific Researcher, Philosopher
|    |    |
|    |    |--> For Llama3-70b-8192: Select System Message for Code Queries
|    |    |    |
|    |    |    |--> Options: Software Engineer, Data Scientist, Web Developer
|    |    |
|    |    |--> For Gemma-7b-it: Select System Message for Simple Queries
|    |         |
|    |         |--> Options: Friendly AI, Virtual Assistant, Empathetic Listener
|    |--> Output: Selected System Message for Model
|
|--> **Generate Response**
|    |
|    |--> Generate Response Using Model and System Message
|    |--> Output: Model Response
|
|--> **Customer Service Department Routing**
|    |
|    |--> Check if Query is Related to Customer Service
|         |
|         |-- Yes --> Route to Department Router
|         |
|         |-- No --> Output: Model Response as Final Answer
|    |
|    |--> Output: Department-Specific Response if Applicable
|
|--> **Department Router (for Customer Service)**
|    |
|    |--> Identify Appropriate Department for Query
|    |    |
|    |    |--> Options: Electronics, Fashion, Home & Garden, Books & Media
|    |--> Assign Department-Specific System Message
|    |--> Generate Response Based on Department Information
|    |--> Output: Department Response as Final Answer
|
|--> End: Intelligent Routing and Response System Completed
