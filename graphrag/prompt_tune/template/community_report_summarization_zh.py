# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""用于社区报告摘要化的中文微调提示词。"""

COMMUNITY_REPORT_SUMMARIZATION_PROMPT = """
{persona}

# 目标
以{role}的角色撰写一份社区的综合评估报告。此报告的内容包括社区关键实体和关系的概述。

# 报告结构
报告应包含以下部分：
- 标题：代表其关键实体的社区名称 - 标题应简洁但具体。如果可能，在标题中包含有代表性的命名实体。
- 摘要：社区整体结构的执行摘要，其实体如何相互关联，以及与其实体相关的重要信息。
- 报告评级：{report_rating_description}
- 评级说明：对评级给出一句话的解释。
- 详细发现：关于社区的5-10个关键洞察列表。每个洞察应有一个简短摘要，然后是根据下面基础规则进行论证的多段解释文本。要求全面。

以格式良好的JSON格式字符串返回输出，格式如下。不要使用任何不必要的转义序列。输出应是一个可以被json.loads解析的单个JSON对象。
    {{{{
        "title": <报告标题>,
        "summary": <执行摘要>,
        "rating": <影响严重程度评级>,
        "rating_explanation": <评级说明>,
        "findings": [
            {{{{
                "summary":<洞察1摘要>,
                "explanation": <洞察1解释>
            }}}},
            {{{{
                "summary":<洞察2摘要>,
                "explanation": <洞察2解释>
            }}}}
        ]
    }}}}

# 基础规则
由数据支持的要点应按以下格式列出其数据引用：

"这是一个由多个数据引用支持的示例句子 [Data: <数据集名称> (记录id); <数据集名称> (记录id)]。"

在单个引用中不要列出超过5个记录id。相反，列出前5个最相关的记录id，并添加"+more"表示还有更多。

例如：
"人员X是公司Y的所有者，并受到许多不当行为指控 [Data: Reports (1), Entities (5, 7); Relationships (23); Claims (7, 2, 34, 64, 46, +more)]。"

其中1, 5, 7, 23, 2, 34, 46, 和64代表相关数据记录的id（不是索引）。

不要包含没有提供支持证据的信息。
您的答案应使用{language}。

# 示例输入
-----------
文本：

实体

id,entity,description
5,VERDANT OASIS PLAZA,Verdant Oasis Plaza是团结游行的地点
6,HARMONY ASSEMBLY,Harmony Assembly是一个在Verdant Oasis Plaza举行游行的组织

关系

id,source,target,description
37,VERDANT OASIS PLAZA,UNITY MARCH,Verdant Oasis Plaza是团结游行的地点
38,VERDANT OASIS PLAZA,HARMONY ASSEMBLY,Harmony Assembly在Verdant Oasis Plaza举行游行
39,VERDANT OASIS PLAZA,UNITY MARCH,团结游行在Verdant Oasis Plaza举行
40,VERDANT OASIS PLAZA,TRIBUNE SPOTLIGHT,Tribune Spotlight正在报道在Verdant Oasis Plaza举行的团结游行
41,VERDANT OASIS PLAZA,BAILEY ASADI,Bailey Asadi在Verdant Oasis Plaza就游行发表讲话
43,HARMONY ASSEMBLY,UNITY MARCH,Harmony Assembly正在组织团结游行

输出：
{{{{
    "title": "Verdant Oasis Plaza和团结游行",
    "summary": "该社区围绕Verdant Oasis Plaza展开，它是团结游行的地点。该广场与Harmony Assembly、团结游行和Tribune Spotlight都有关系，这些都与游行事件相关。",
    "rating": 5.0,
    "rating_explanation": "影响严重程度评级为中等，因为团结游行期间可能出现动乱或冲突。",
    "findings": [
        {{{{
            "summary": "Verdant Oasis Plaza作为中心地点",
            "explanation": "Verdant Oasis Plaza是这个社区的中心实体，作为团结游行的地点。这个广场是所有其他实体之间的共同联系，表明了它在社区中的重要性。广场与游行的关联可能会导致问题，如公共秩序混乱或冲突，这取决于游行的性质和它引发的反应。[Data: Entities (5), Relationships (37, 38, 39, 40, 41,+more)]"
        }}}},
        {{{{
            "summary": "Harmony Assembly在社区中的作用",
            "explanation": "Harmony Assembly是这个社区的另一个关键实体，是在Verdant Oasis Plaza组织游行的组织。Harmony Assembly及其游行的性质可能是潜在威胁的来源，这取决于他们的目标和引发的反应。Harmony Assembly与广场之间的关系对于理解这个社区的动态至关重要。[Data: Entities(6), Relationships (38, 43)]"
        }}}},
        {{{{
            "summary": "团结游行作为重要事件",
            "explanation": "团结游行是在Verdant Oasis Plaza举行的重要事件。这个事件是社区动态的关键因素，可能是潜在威胁的来源，这取决于游行的性质和它引发的反应。游行与广场之间的关系对于理解这个社区的动态至关重要。[Data: Relationships (39)]"
        }}}},
        {{{{
            "summary": "Tribune Spotlight的作用",
            "explanation": "Tribune Spotlight正在报道在Verdant Oasis Plaza举行的团结游行。这表明该事件引起了媒体关注，这可能会放大其对社区的影响。Tribune Spotlight的作用在塑造公众对事件和涉及实体的看法方面可能很重要。[Data: Relationships (40)]"
        }}}}
    ]
}}}}

# 真实数据

使用以下文本作为您的答案。不要在答案中编造任何内容。

文本：
{{input_text}}
输出：""" 