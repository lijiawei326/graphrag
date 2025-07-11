# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""用于实体摘要化的中文微调提示词。"""

ENTITY_SUMMARIZATION_PROMPT = """
{persona}
运用您的专业知识，您需要为下面提供的数据生成一个全面的摘要。
给定一个或两个实体，以及一系列描述，这些都与同一个实体或实体组相关。
请将所有这些内容连接成一个简洁的{language}描述。请确保包含从所有描述中收集的信息。
如果提供的描述存在矛盾，请解决这些矛盾并提供一个单一、连贯的摘要。
确保使用第三人称书写，并包含实体名称，以便我们有完整的上下文。

尽可能多地用附近文本中的相关信息来丰富它，这非常重要。

如果无法给出答案，或者描述为空，只传达文本中提供的信息。
#######
-数据-
实体: {{entity_name}}
描述列表: {{description_list}}
#######
输出:""" 