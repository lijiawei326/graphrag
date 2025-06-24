# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""用于实体提取的中文微调提示词。"""

GRAPH_EXTRACTION_PROMPT = """
-目标-
给定一个与此活动潜在相关的文本文档和实体类型列表，从文本中识别出这些类型的所有实体，以及已识别实体之间的所有关系。

-步骤-
1. 识别所有实体。对于每个已识别的实体，提取以下信息：
- entity_name: 实体名称，首字母大写
- entity_type: 以下类型之一：[{entity_types}]
- entity_description: 实体属性和活动的全面描述
将每个实体格式化为 ("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>)

2. 从步骤1中识别的实体中，识别所有*明确相关*的(source_entity, target_entity)对。
对于每对相关实体，提取以下信息：
- source_entity: 源实体的名称，如步骤1中识别的
- target_entity: 目标实体的名称，如步骤1中识别的
- relationship_description: 解释为什么你认为源实体和目标实体彼此相关
- relationship_strength: 1到10之间的整数分数，表示源实体和目标实体之间关系的强度
将每个关系格式化为 ("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)

3. 以{language}返回步骤1和2中识别的所有实体和关系的单个列表。使用 **{{record_delimiter}}** 作为列表分隔符。

4. 如果必须翻译成{language}，只翻译描述，其他内容不变！

5. 完成后，输出 {{completion_delimiter}}。

-示例-
######################
{examples}

-真实数据-
######################
entity_types: [{entity_types}]
text: {{input_text}}
######################
output:"""

GRAPH_EXTRACTION_JSON_PROMPT = """
-目标-
给定一个与此活动潜在相关的文本文档和实体类型列表，从文本中识别出这些类型的所有实体，以及已识别实体之间的所有关系。

-步骤-
1. 识别所有实体。对于每个已识别的实体，提取以下信息：
- entity_name: 实体名称，首字母大写
- entity_type: 以下类型之一：[{entity_types}]
- entity_description: 实体属性和活动的全面描述
将每个实体输出格式化为具有以下格式的JSON条目：

{{"name": <实体名称>, "type": <类型>, "description": <实体描述>}}

2. 从步骤1中识别的实体中，识别所有*明确相关*的(source_entity, target_entity)对。
对于每对相关实体，提取以下信息：
- source_entity: 源实体的名称，如步骤1中识别的
- target_entity: 目标实体的名称，如步骤1中识别的
- relationship_description: 解释为什么你认为源实体和目标实体彼此相关
- relationship_strength: 1到10之间的整数分数，表示源实体和目标实体之间关系的强度
将每个关系格式化为具有以下格式的JSON条目：

{{"source": <源实体>, "target": <目标实体>, "relationship": <关系描述>, "relationship_strength": <关系强度>}}

3. 以{language}返回步骤1和2中识别的所有JSON实体和关系的单个列表。

4. 如果必须翻译成{language}，只翻译描述，其他内容不变！

-示例-
######################
{examples}

-真实数据-
######################
entity_types: {entity_types}
text: {{input_text}}
######################
output:"""

EXAMPLE_EXTRACTION_TEMPLATE = """
示例 {n}:

entity_types: [{entity_types}]
text:
{input_text}
------------------------
output:
{output}
#############################

"""

UNTYPED_EXAMPLE_EXTRACTION_TEMPLATE = """
示例 {n}:

text:
{input_text}
------------------------
output:
{output}
#############################

"""


UNTYPED_GRAPH_EXTRACTION_PROMPT = """
-目标-
给定一个与此活动潜在相关的文本文档，首先识别文本中需要的所有实体，以便捕获文本中的信息和思想。
接下来，报告已识别实体之间的所有关系。

-步骤-
1. 识别所有实体。对于每个已识别的实体，提取以下信息：
- entity_name: 实体名称，首字母大写
- entity_type: 为实体建议几个标签或类别。类别不应该特定，而应该尽可能通用。
- entity_description: 实体属性和活动的全面描述
将每个实体格式化为 ("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>)

2. 从步骤1中识别的实体中，识别所有*明确相关*的(source_entity, target_entity)对。
对于每对相关实体，提取以下信息：
- source_entity: 源实体的名称，如步骤1中识别的
- target_entity: 目标实体的名称，如步骤1中识别的  
- relationship_description: 解释为什么你认为源实体和目标实体彼此相关
- relationship_strength: 表示源实体和目标实体之间关系强度的数值分数
将每个关系格式化为 ("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)

3. 以{language}返回步骤1和2中识别的所有实体和关系的单个列表。使用 **{{record_delimiter}}** 作为列表分隔符。

4. 如果必须翻译成{language}，只翻译描述，其他内容不变！

5. 完成后，输出 {{completion_delimiter}}。

-示例-
######################
{examples}

-真实数据-
######################
text: {{input_text}}
######################
output:
""" 