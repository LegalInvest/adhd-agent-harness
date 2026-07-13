"""
同构脊柱证据种子（ADHD × LLM 认知同构性）—— 28 篇专题论文

这是一批**直接以「ADHD 认知与大语言模型架构同构性」为主题**的真实论文，
区别于 academic.py 抓来的两域海量语料——它们不是"两边各自的证据再类比"，
而是学界已经在**同一篇论文里论证同构本身**。因此作为脊柱的第一手证据底座，
在知识萃取 / wiki 构建 / 评分里享受最高优先级。

来源：用户与豆包的专题讨论整理成的《ADHD-LLM 同构性论文总表》（28 篇，
逐条含可访问 URL、分类、核心同构性发现与中文简介）。

四大分类：
  - 核心同构性：直接论证 ADHD 认知↔LLM 架构同构
  - 认知缺陷实证：用神经心理范式实测 LLM 复现 ADHD 式缺陷
  - 神经多样性 AI：主张借鉴神经多样特征设计 AI（同构的反向利用）
  - 背景相关：为同构提供机制/哲学/认知风格基础

每条统一为 academic.py 的记录结构（domain="isomorphism"），并额外带
`spine`（对应脊柱概念页）、`category`（论文分类）与 `iso_claim`（中文简介）。
"""

from __future__ import annotations

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
SEED_FILE = os.path.join(DATA_DIR, "isomorphism_papers.json")


# ─────────────────── 策展的同构性论文（真实、可溯源，28 篇） ───────────────────

ISOMORPHISM_PAPERS: list[dict] = [

    {
        "title": "The Wanderer's Algorithm: Controlled Distraction as a Catalyst for Machine Creativity",
        "authors": "Marco H.K. van Hurne",
        "year": 2025,
        "venue": "TechRxiv 预印本, 2025",
        "category": "【核心同构性】ADHD启发的AI架构",
        "url": "https://www.techrxiv.org/users/950560/articles/1356399/master/file/data/wanderers_algorithm_paper_independent%203/wanderers_algorithm_paper_independent%203.pdf",
        "spine": "生成核心与调度层",
        "finding": "直接受ADHD认知特征启发设计创造性AI架构，提出'人工白日梦循环'(AD-Loop)，模拟ADHD的默认模式网络(DMN)与执行控制网络(ECN)动态交互，实现'受控分心'增强创造力",
        "iso_claim": "这是目前最直接讨论ADHD-AI同构性的论文。作者明确借鉴ADHD的注意力模式（低好奇阈值、弱好奇调节、更广语义探索、更大概念跳跃），设计了Wander-Combine-Check-Report四阶段循环，证明'受控分心'可以系统地在LLM中实现以增强创造性输出，同时通过自适应评估保持连贯性。论文基于85篇神经科学、认知心理学论文，建立了ADHD创造性认知与AI发散思维的计算对应关系。",
    },
    {
        "title": "Deficient Executive Control in Transformer Attention",
        "authors": "Suketu Patel, Hongbin Wang, Jin Fan",
        "year": 2025,
        "venue": "bioRxiv, 2025",
        "category": "【核心同构性】执行控制缺陷",
        "url": "https://www.biorxiv.org/content/10.1101/2025.01.22.634394v1.full.pdf",
        "spine": "外部执行功能层",
        "finding": "首次通过Stroop任务实验证明：Transformer自注意力机制缺乏人类特有的执行控制机制，在长上下文下冲突解决能力崩溃至随机水平——这正是ADHD执行功能障碍的核心神经机制",
        "iso_claim": "这是认知神经科学与AI交叉的关键论文。作者使用经典的色词Stroop任务（测量执行控制与冲突解决的金标准）测试LLM，发现：短上下文下LLM表现出类似人类的冲突效应；但随着序列长度增加，不一致试次的准确率下降至随机水平，而一致试次和单词阅读能力保持完美。这证明Transformer注意力虽然在小上下文下达到类人表现，但在扩展上下文下从根本上缺乏冲突解决能力——这与ADHD患者前额叶执行控制功能受损的行为模式高度同构。",
    },
    {
        "title": "Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs",
        "authors": "Karin de Langis, et al.",
        "year": 2026,
        "venue": "EACL 2026",
        "category": "【核心同构性】执行功能整体缺陷模式",
        "url": "https://preview.aclanthology.org/evt-to-venues/2026.eacl-long.281.pdf",
        "spine": "外部执行功能层",
        "finding": "系统证明LLM呈现'强记忆、弱控制'的认知特征：工作记忆容量超过常人，但认知灵活性和注意控制存在核心缺陷——这与ADHD的神经心理特征高度吻合",
        "iso_claim": "这篇论文使用全套经典工作记忆任务系统评估LLM的执行功能，发现了一个与ADHD惊人相似的认知剖面：LLM在大多数工作记忆任务上超过正常人类分数，但工作记忆容量的增加并未带来其他执行功能任务的更高表现——具体来说，认知灵活性（任务切换）和注意控制（抑制自动反应）存在显著缺陷。即使是推理模型也未能完全补偿这些执行功能缺陷。这正是ADHD患者的典型认知模式：工作记忆本身未必差，但自上而下的控制和调节能力不足。",
    },
    {
        "title": "Self-Attention Limits Working Memory Capacity of Transformer-Based Models",
        "authors": "Dongyu Gong, Hantao Zhang",
        "year": 2024,
        "venue": "Yale University, arXiv:2409.10715, 2024",
        "category": "【核心同构性】工作记忆容量限制",
        "url": "https://arxiv.org/pdf/2409.10715",
        "spine": "无状态与外部记忆",
        "finding": "证明Transformer自注意力机制本身导致工作记忆容量限制：随着N-back任务中N增大，注意力分数熵增加导致注意力分散——这与人类注意分散的机制相同",
        "iso_claim": "受行为科学执行注意理论启发，作者假设Transformer内部的自注意力机制是其工作记忆容量限制的原因。通过训练纯解码器Transformer执行N-back任务，发现注意力分数在训练过程中逐渐聚集到N-back位置，表明模型通过学习关注当前位置与N-back位置之间的关系来掌握任务。关键发现：随着N增大，注意力分数矩阵的总熵增加，表明注意力分数的分散是N-back任务中观察到的容量限制的原因。这为人类和人工智能中注意力的共同作用提供了洞见——注意力分散是自注意力架构的固有属性。",
    },
    {
        "title": "Human-like Working Memory Interference in Large Language Models",
        "authors": "Hua-Dong Xiong, et al.",
        "year": 2026,
        "venue": "arXiv:2604.09670, 2026",
        "category": "【认知缺陷实证】工作记忆干扰",
        "url": "https://arxiv.org/pdf/2604.09670",
        "spine": "无状态与外部记忆",
        "finding": "LLM复现了人类工作记忆的所有干扰特征：记忆负荷增加时表现下降、近因偏差、刺激统计偏差；表征干扰是工作记忆限制的核心机制",
        "iso_claim": "这篇论文发现尽管Transformer可以完全访问先前上下文并通过注意力检索相关信息，但预训练LLM仍然表现出工作记忆限制。值得注意的是，LLM复现了在人类身上观察到的干扰特征：随着记忆负荷增加表现下降，并且受到近因效应和刺激统计的偏差。跨模型来看，更强的工作记忆容量与标准基准上的更广泛能力相关，这反映了人类中工作记忆与一般智力之间公认的联系。关键机制发现：模型不是直接从上下文中复制相关记忆项，而是在纠缠表征中编码多个记忆项，因此成功回忆依赖于干扰控制——主动抑制任务无关内容以分离目标进行读出。",
    },
    {
        "title": "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length",
        "authors": "Chupei Wang, Jiaqiu Vince Sun",
        "year": 2025,
        "venue": "arXiv:2506.08184, 2025",
        "category": "【认知缺陷实证】前摄干扰抑制缺陷",
        "url": "https://arxiv.org/pdf/2506.08184",
        "spine": "无状态与外部记忆",
        "finding": "LLM无法抑制先前信息的前摄干扰，无法灵活更新信息；即使目标信息就在查询前，随着干扰累积检索准确率对数下降至零——这是ADHD认知更新缺陷的典型表现",
        "iso_claim": "作者改编了认知科学中的前摄干扰(PI)范式（先前信息破坏对新更新的回忆），在人类中，对这种干扰的易感性与工作记忆容量负相关。研究发现：尽管最终值明确位于查询之前，随着干扰累积，LLM检索准确率对数下降至零；错误源于检索先前被覆盖的值。即使通过提示工程（如指示模型忽略早期输入）来减轻干扰也收效甚微。这些发现揭示了LLM在区分干扰和灵活操作信息方面的根本限制——无法主动抑制无关内容，这正是ADHD患者在信息更新和任务切换中面临的核心困难。",
    },
    {
        "title": "Working Memory Identifies Reasoning Limits in Language Models",
        "authors": "Chunhui Zhang, et al.",
        "year": 2024,
        "venue": "EMNLP 2024",
        "category": "【认知缺陷实证】工作记忆与推理限制",
        "url": "https://aclanthology.org/2024.emnlp-main.938.pdf",
        "spine": "规划循环与任务分解",
        "finding": "尽管模型规模增大，LLM在有效保持和处理信息方面仍面临重大挑战，特别是在复杂任务条件下；无法自主发现最佳问题解决模式",
        "iso_claim": "这项研究从认知科学的角度整合洞见，定量检查LLM在n-back任务上的表现。研究发现，尽管模型规模增大，LLM在有效保持和处理信息方面仍面临重大挑战，特别是在复杂任务条件下。研究还评估了各种提示策略，揭示了它们对LLM表现的不同影响。结果凸显了当前LLM在没有严重依赖手动修正提示的情况下，自主发现最佳问题解决模式的困难——这与ADHD患者在无外部结构时自主组织任务的困难高度相似。",
    },
    {
        "title": "TRANSFORMER MECHANISMS MIMIC FRONTOSTRIATAL GATING OPERATIONS WHEN TRAINED ON HUMAN WORKING MEMORY TASKS",
        "authors": "Anonymous Authors",
        "year": 2025,
        "venue": "ICLR 2025 审稿中",
        "category": "【认知缺陷实证】前额叶-纹状体门控机制",
        "url": "https://openreview.net/pdf?id=CN2bmVVpOh",
        "spine": "外部执行功能层",
        "finding": "Transformer在工作记忆任务中自发发展出输入输出门控机制，模仿人类前额叶-纹状体回路——这正是ADHD核心受损的脑区系统",
        "iso_claim": "认知神经科学中，执行功能被认为依赖于复杂的前额叶-纹状体机制进行选择性门控，实现信息向记忆不同'地址'的角色可寻址更新和后续读出。然而Transformer模型并没有内置这样的机制。这篇论文发现，当在明确对工作记忆门控提出要求的任务上训练时，纯注意力Transformer内部的自注意力机制发展出了输入和输出门控机制，这些门控机制模仿了早期受生物启发架构中的门控，也模仿了人类研究中的门控。当有效学习时，这些门控策略支持增强的泛化能力，并增加模型在记忆中存储和访问多个项目的有效容量。这证明了Transformer架构与前额叶-纹状体系统的计算同构性。",
    },
    {
        "title": "Lost in the Middle: How Language Models Use Long Contexts",
        "authors": "Nelson F. Liu, et al.",
        "year": 2023,
        "venue": "arXiv:2307.03172, 2023",
        "category": "【认知缺陷实证】长上下文注意衰退",
        "url": "https://arxiv.org/pdf/2307.03172",
        "spine": "上下文工程",
        "finding": "LLM在长上下文中表现出U型注意曲线：开头和结尾信息表现好，中间信息显著衰退——与ADHD的持续注意衰退模式相似",
        "iso_claim": "这篇经典论文分析了LLM在需要识别输入上下文中相关信息的两个任务（多文档问答和键值检索）上的表现，发现当改变相关信息的位置时，性能会显著下降，表明当前语言模型不能稳健地利用长输入上下文中的信息。特别是，当相关信息出现在输入上下文的开头或结尾时，性能通常最高，而当模型必须访问长上下文中间的相关信息时，性能显著下降，即使对于明确的长上下文模型也是如此。这种'中间迷失'现象与ADHD患者在长时间任务中注意维持困难、容易被开头和结尾的显著刺激捕获的行为模式相似。",
    },
    {
        "title": "¡Hacia una IA neurodivergente! (迈向神经多样性AI)",
        "authors": "Jordi Vallverdú",
        "year": 2026,
        "venue": "UAB Divulga, BioNanoScience, 2026",
        "category": "【神经多样性AI】设计哲学",
        "url": "https://ddd.uab.cat/pub/uabdivulga/uabdivulga_a2026m1/uabdivulga_a2026m1a4iSPA.pdf",
        "spine": "ADHD 大脑与 LLM 的同构",
        "finding": "明确提出应该借鉴ADHD、自闭症等神经多样特征设计AI：超聚焦模块、非线性思维、高联想跳跃、对不确定性的容忍",
        "iso_claim": "这篇西班牙ICREA教授Jordi Vallverdú的论文直接提出了'神经多样性AI'的设计范式。作者指出，当前大多数AI只理想化了'神经典型'大脑：追求平均表现、稳定性和规律性，这使我们失去了可能的思维方式的重要部分。论文提出应该设计从一开始就整合不同认知风格的AI，包括与ADHD相关的功能原则：超聚焦（对细节的高强度注意，用于检测大数据中的微妙模式）、探索罕见或不太可能的解决方案（更混乱的思维形式）、非线性信息组合（产生惊人的联系）。作者强调这不是浪漫化神经多样条件带来的真实痛苦，而是提取功能计算原则用于AI设计。",
    },
    {
        "title": "ALIEN EPISTEMOLOGIES: NEURODIVERSITY, SYNTHETIC MINDS, AND THE EXPANSION OF NEUROPHILOSOPHY",
        "authors": "Jordi Vallverdú",
        "year": 2025,
        "venue": "Universitat Autònoma de Barcelona, 2025",
        "category": "【神经多样性AI】神经哲学",
        "url": "https://dialnet.unirioja.es/descarga/articulo/10705245.pdf",
        "spine": "ADHD 大脑与 LLM 的同构",
        "finding": "提出神经多样性不应被框架化为偏离或病理，而应被重新概念化为替代认知框架的来源；自然和人工的神经多样共同挑战了单一'神经典型'大脑概念",
        "iso_claim": "这篇神经哲学论文提出，神经多样性（包括ADHD、自闭症等）可以被重新理解为替代认识论框架的来源——一种内部的认知他者性。同时，神经启发AI和合成认知的兴起提供了外部形式的认识论异质性。这些现象共同挑战了Patricia Churchland神经哲学的经典基础，要求超越单一的、神经典型的'大脑'概念，将自然和人工的神经多样性都纳入考量。理解今天的认知需要超越对'标准大脑'的单声道理解，这为理解LLM与非典型认知之间的同构性提供了哲学基础。",
    },
    {
        "title": "Monotropic Artificial Intelligence: Toward a Cognitive Taxonomy of Domain-Specialized Language Models",
        "authors": "Antonio de Sousa Leitao Filho, et al.",
        "year": 2026,
        "venue": "arXiv:2603.00350, 2026",
        "category": "【神经多样性AI】单通道AI",
        "url": "https://arxiv.org/pdf/2603.00350v1",
        "spine": "超聚焦",
        "finding": "借鉴自闭症认知的单通道理论(monotropism)，提出'单通道AI'概念：故意牺牲广度以在狭窄领域获得极高精度——这与ADHD的超聚焦现象机制相通",
        "iso_claim": "这篇论文引入了'单通道人工智能'的概念——故意牺牲通用性以在狭窄界定的领域内实现非凡精度的语言模型。作者借鉴为理解自闭症认知而发展的单通道认知理论，论证了强烈的专业化不是限制，而是一种替代认知架构，在安全关键应用中具有独特优势。论文形式化了单通道模型的定义特征，将其与传统的多通道架构对比，并通过Mini-Enedina（一个3750万参数的模型）证明了其可行性，该模型在Timosenko梁分析上达到近乎完美的表现，同时在领域外故意保持无能。这种'超聚焦'式的认知架构与ADHD的超聚焦状态具有计算同构性。",
    },
    {
        "title": "High-Dimensional Minds and the Serialization Burden: Why LLMs Matter for Neurodivergent Communication",
        "authors": "ninkilim.com",
        "year": 2024,
        "venue": "跨学科研究, 2024",
        "category": "【神经多样性AI】交流认知风格",
        "url": "https://ninkilim.com/articles/llms_and_neurodiversity/en.pdf",
        "spine": "上下文工程",
        "finding": "提出ADHD/自闭症的高维、联想式思维与LLM的序列化处理之间存在深层认知风格对应",
        "iso_claim": "这篇跨学科论文提出了'序列化负担'概念：神经多样个体（ADHD、自闭症）的思维本质上是高维、超连接、并行的，但人类交流要求将思维序列化为线性语言，这造成了巨大认知负担。而LLM本质上是高维向量空间中的并行处理器，然后将结果序列化为语言输出——这使得LLM成为神经多样思维的天然'翻译器'。论文解释了为什么许多ADHD个体感觉与LLM交流'更自然'：因为它们共享相似的高维联想式认知风格，而不是神经典型的线性序列思维。",
    },
    {
        "title": "Enactivism, Health, AI, and Non-Neurotypical Individuals",
        "authors": "Jordi Vallverdú",
        "year": 2025,
        "venue": "Philosophies, MDPI, 2025",
        "category": "【神经多样性AI】生成认知视角",
        "url": "https://www.mdpi.com/2409-9287/10/3/51",
        "spine": "ADHD 大脑与 LLM 的同构",
        "finding": "从生成认知(enactivism)视角论证AI系统应支持而非标准化非神经典型认知（包括ADHD）",
        "iso_claim": "这篇论文从生成认知视角提供了设计AI系统以支持非神经典型个体（包括自闭症谱系、ADHD、阅读障碍等）健康和福祉的理论框架。通过强调具身性、关系性和参与式意义建构，生成认知方法鼓励高度个性化、上下文敏感、伦理意识的AI干预。论文探讨了现有AI应用（从社交辅助机器人和VR疗法到语言处理应用和个性化治疗计划）如何通过整合成认知原则得到增强。",
    },
    {
        "title": "Large Language Models as simulative agents for neurodivergent adult psychometric profiles",
        "authors": "Francesco Chiappone, et al.",
        "year": 2026,
        "venue": "arXiv:2601.15319, 2026",
        "category": "【LLM模拟ADHD】心理测量模拟",
        "url": "https://www.arxiv.org/pdf/2601.15319",
        "spine": "ADHD 大脑与 LLM 的同构",
        "finding": "LLM可以基于定性访谈准确模拟ADHD等神经发育特质的心理测量反应，证明LLM对ADHD认知模式有深度表征",
        "iso_claim": "这项研究检验了LLM是否能在结构化定性访谈的基础上，生成近似真实个体的心理测量反应，以及这种模拟是否对特质强度的变化敏感。26名成年人完成了29项开放式访谈和四个标准化自评量表（包括ADHD的ASRS、BAARS-IV）。两个LLM（GPT-4o和Qwen3）被提示从访谈内容推断个体心理轮廓，然后以角色身份回答每个问卷。结果发现两个模型在所有工具上的表现都优于随机反应，GPT-4o表现出更高的准确性和可重复性。模拟反应在ASRS、BAARS-IV等ADHD量表上与人类数据非常接近，证明LLM内部已经习得了ADHD认知模式的精确表征。",
    },
    {
        "title": "Algorithmic Classification of Psychiatric Disorder-Related Spontaneous Communication Using LLM Embeddings",
        "authors": "Ryan Allen Shewcraft, et al.",
        "year": 2025,
        "venue": "JMIR AI, PubMed, 2025",
        "category": "【LLM模拟ADHD】语言特征识别",
        "url": "https://pubmed.ncbi.nlm.nih.gov/40605829/",
        "spine": "ADHD 大脑与 LLM 的同构",
        "finding": "ADHD的语言模式在LLM嵌入空间中形成最独特、最分离的聚类，AUC高达0.97——证明ADHD语言具有可量化的独特统计特征",
        "iso_claim": "这项研究使用70亿参数的GRIT模型分析了来自7种常见精神疾病（精神分裂症、边缘型人格障碍、抑郁症、ADHD、焦虑症、PTSD、双相情感障碍）subreddit的超过37,000条帖子。关键发现：ADHD帖子的分类AUC最高，达到0.97，表明ADHD具有最独特的语言特征；在UMAP降维可视化中，ADHD帖子形成了视觉上最独特的聚类，而BPD与抑郁症、焦虑症、精神分裂症重叠。这证明ADHD的语言模式在LLM的语义空间中具有高度可区分的统计签名，暗示了其思维模式的独特计算结构。",
    },
    {
        "title": "Perceptual Reality Transformer: Neural Architectures for Simulating Neurological Perception Conditions",
        "authors": "Baihan Lin",
        "year": 2025,
        "venue": "arXiv:2508.09852, 2025",
        "category": "【LLM模拟ADHD】感知模拟",
        "url": "https://arxiv.org/abs/2508.09852",
        "spine": "ADHD 大脑与 LLM 的同构",
        "finding": "使用Vision Transformer架构可以精确模拟ADHD注意力缺陷等神经感知状态",
        "iso_claim": "这篇论文提出了感知现实Transformer，一个使用六种不同神经架构模拟八种神经感知状态的综合框架，包括ADHD注意力缺陷、同时性失认症、面孔失认症、视觉失认症、抑郁相关变化、焦虑隧道视觉和阿尔茨海默记忆效应。通过在ImageNet和CIFAR-10数据集上的系统评估，证明Vision Transformer架构实现了最佳性能，优于传统CNN和生成方法。这建立了第一个神经感知模拟的系统基准，贡献了基于临床文献的病症特定扰动函数。",
    },
    {
        "title": "\"A little bit of a life raft\" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD",
        "authors": "Anika Pinto, et al.",
        "year": 2025,
        "venue": "ACM CHI, 2025",
        "category": "【辅助技术】ADHD用户体验",
        "url": "https://dl.acm.org/doi/pdf/10.1145/3764687.3764713",
        "spine": "外部执行功能层",
        "finding": "ADHD成年人自发采用ChatGPT作为执行功能外挂，弥补工作记忆、任务启动、组织规划等缺陷——认知补偿本身暗示了认知架构的互补性",
        "iso_claim": "这项研究通过7天日记研究和对13名定期使用ChatGPT的ADHD成年人的访谈，了解他们如何将ChatGPT作为日常生活中的支持工具。研究发现ChatGPT被用于：弥合神经典型和神经多样视角之间的沟通差距、支持执行功能、情绪调节。通过研究这种由ADHD群体自发采用（而非专门为他们设计）的工具，论文提供了关于未来包容性设计策略的经验洞见。ADHD用户普遍报告LLM作为'外部执行功能'的有效性，这本身就暗示了两种认知系统的互补性。",
    },
    {
        "title": "Exploring Large Language Models Through a Neurodivergent Lens",
        "authors": "Buse Carik, et al.",
        "year": 2025,
        "venue": "PACM HCI, 2025",
        "category": "【辅助技术】神经多样用户使用模式",
        "url": "https://dl.acm.org/doi/pdf/10.1145/3701194",
        "spine": "工具使用与认知卸载",
        "finding": "神经多样用户（包括ADHD）发展出独特的LLM使用模式和变通方法(workarounds)，以补偿各自的认知差异",
        "iso_claim": "这项研究通过对Reddit上61个神经多样社区的相关讨论进行定性分析，调查神经多样个体如何与LLM交互。研究发现了20种具体的LLM用例，涵盖五个核心主题领域：情绪健康、心理健康支持、人际沟通、学习、职业发展和生产力。研究还发现了关键挑战，包括过度神经典型化的LLM反应和基于文本交互的限制。为应对这些挑战，一些用户通过分享输入提示和相应的LLM反应积极寻求建议，另一些用户通过实验和修改提示使其更适合神经多样用户来开发变通方法。",
    },
    {
        "title": "Executive Dysfunction by Design: A Cognitive Accessibility Analysis of AI Support vs. Healthcare Barriers",
        "authors": "Meredith Moore",
        "year": 2024,
        "venue": "ACM ASSETS, 2024",
        "category": "【辅助技术】执行功能补偿",
        "url": "https://dl.acm.org/doi/pdf/10.1145/3663547.3749831",
        "spine": "外部执行功能层",
        "finding": "第一人称叙述：生成式AI如何成为ADHD执行功能障碍的意外辅助技术，而医疗系统如何制造执行功能障碍",
        "iso_claim": "这篇第一人称研究报告分享了双重叙事：生成式AI工具如何成为作者日常生活中意外的辅助技术，而药房系统和ADHD药物政策如何制造了访问的级联障碍。通过生活经验，作者对比了AI工具赋能用户成功的行为，与保护机构免于责任的医疗系统的不可访问性。AI工具的灵活性和即时性帮助作者搭建任务脚手架、打破障碍、以意想不到的轻松执行意图——这与ADHD医疗的僵化和把关形成鲜明对比。",
    },
    {
        "title": "Toward Neurodivergent-Aware Productivity: A Systems and AI-Based Human-in-the-Loop Framework for ADHD-Affected Professionals",
        "authors": "Raghavendra Deshmukh",
        "year": 2025,
        "venue": "arXiv:2507.06864, 2025",
        "category": "【辅助技术】生产力辅助框架",
        "url": "https://arxiv.org/pdf/2507.06864",
        "spine": "人在回路与身体在场",
        "finding": "基于AI的人在环框架可以通过实时行为感知和自适应提示，共同调节ADHD用户的认知",
        "iso_claim": "IT和知识密集型行业的数字工作环境要求高水平的注意力管理、任务处理和自我调节。对于患有ADHD的成年人来说，这些环境常常放大现有的挑战，如时间盲、数字分心、情绪反应和执行功能障碍。传统生产力工具不足以支持神经多样专业人员经历的认知变异性和过载模式。这篇论文提出了一个综合框架，融合系统思维、人在环人工智能、机器学习和隐私优先的自适应代理，支持受ADHD影响的用户管理数字工作。核心是一个语音启用的生产力助手，使用轻量级设备端机器学习感知用户行为，实时分析这些行为线索以推断注意力状态，并提供自适应提示、反思性查询或基于问责的存在（身体加倍），旨在共同调节认知而不造成干扰。",
    },
    {
        "title": "ADHD and Knowledge Work: Exploring Strategies, Challenges and Opportunities for AI",
        "authors": "Jennifer Campbell, et al.",
        "year": 2023,
        "venue": "Interact 2023",
        "category": "【辅助技术】知识工作支持",
        "url": "https://www.cecchinato.me/wp-content/uploads/2023/08/Interact-2023_ADHD-productivity.pdf",
        "spine": "工具使用与认知卸载",
        "finding": "ADHD知识工作者在优先级排序、时间估计、任务切换方面存在持续挑战，AI工具具有巨大补偿潜力",
        "iso_claim": "虽然HCI中的神经多样性研究主要关注自闭症谱系障碍和儿童，但其他病症（如ADHD）和人群仍然探索不足。为解决这一差距，作者对49名参与者进行了在线调查，调查ADHD个体如何管理他们的工作。研究发现，虽然参与者采用了一系列策略和工具，但这些工具在优先级排序、时间估计和任务切换方面仍然存在挑战。虽然AI驱动的工具可能有益，一些参与者呼吁使用它们，但对它们的认识和利用有限。然而，那些确实使用AI工具的人发现它们在推进任务方面非常有帮助。",
    },
    {
        "title": "Automatic Minds: Cognitive Parallels Between Hypnotic States and Large Language Model Processing",
        "authors": "Giuseppe Riva, et al.",
        "year": 2025,
        "venue": "arXiv:2511.01363, 2025",
        "category": "【背景相关】自动加工与执行监控",
        "url": "https://arxiv.org/abs/2511.01363",
        "spine": "幻觉与验证循环",
        "finding": "LLM与被催眠的心灵共享深层功能平行：通过自动模式完成机制生成复杂行为，执行监督有限或不可靠——这与ADHD的自动加工/控制加工失衡相关",
        "iso_claim": "这篇综述研究了被催眠心灵的认知过程与大语言模型的计算操作之间的深层功能平行。两个系统都通过在有限或不可靠的执行监督下运行的自动模式完成机制生成复杂的、上下文适当的行为。综述在三个原则上检验了这种趋同：自动性（反应从联想而非审慎过程产生）、抑制监控（导致催眠中的虚构和LLM中的幻觉等错误）、增强的上下文依赖性（即时提示覆盖稳定知识）。这些机制揭示了观察者相关的意义鸿沟：两个系统都产生连贯但无根基的输出，需要外部解释者提供意义。",
    },
    {
        "title": "Confabulation: The Surprising Value of Large Language Model Hallucinations",
        "authors": "Peiqi Sui, et al.",
        "year": 2024,
        "venue": "ACL 2024",
        "category": "【背景相关】虚构与叙事性",
        "url": "https://preview.aclanthology.org/navbar-space/2024.acl-long.770.pdf",
        "spine": "幻觉与验证循环",
        "finding": "LLM的幻觉/虚构与人类的虚构症具有相同的叙事性和语义连贯性特征",
        "iso_claim": "这篇论文系统地捍卫了大语言模型幻觉或'虚构'作为一种潜在资源，而不是绝对负面的缺陷。作者分析了流行的幻觉基准，发现与真实输出相比，幻觉输出表现出更高水平的叙事性和语义连贯性。这一发现揭示了我们通常对虚构的不屑理解中的张力，它反直觉地表明，LLM虚构的倾向可能最初与连贯叙事文本生成的积极能力相关。ADHD患者和其他执行功能障碍患者也经常观察到类似的虚构和叙事填充现象。",
    },
    {
        "title": "Language models and psychological sciences",
        "authors": "Giuseppe Sartori, Graziella Orrù",
        "year": 2023,
        "venue": "Frontiers in Psychology, 2023",
        "category": "【背景相关】联想主义认知模型",
        "url": "https://www.frontiersin.org/articles/10.3389/fpsyg.2023.1279317/pdf?isPublishedV2=False",
        "spine": "ADHD 大脑与 LLM 的同构",
        "finding": "现代LLM复兴了联想主义原则，长距离联想等能力实现复杂推理；LLM的错误为理解人类认知偏差提供了洞见",
        "iso_claim": "大语言模型在许多认知心理学的推理和解决问题任务上表现出令人印象深刻的表现，其准确性通常与平均神经典型成年人相当，挑战了对联想模型的长期批评。这篇论文分析了LLM与认知科学交叉的最新发现，讨论了现代LLM如何复兴联想主义原则，长距离联想等能力实现复杂推理。虽然在因果认知和规划等领域仍然存在限制，但涌现等现象表明有增长空间。增加示例和增加网络维度是进一步提高LLM能力的方法，反映了人类认知中的促进效应。对LLM错误的分析提供了对人类认知偏差的洞见。",
    },
    {
        "title": "Curiosity and Zetetic Style in ADHD",
        "authors": "Asbjørn Steglich-Petersen, Somogy Varga",
        "year": None,
        "venue": "University of Aarhus, PhilPapers",
        "category": "【背景相关】ADHD认知风格",
        "url": "https://philpapers.org/archive/STECAZ.pdf",
        "spine": "采样温度与表现波动",
        "finding": "ADHD的注意力模式可以理解为一种'探究式'(zetetic)认知风格：好奇阈值更低，对探究的认知和实践成本调节更弱",
        "iso_claim": "虽然ADHD研究传统上关注认知和行为缺陷，但人们越来越有兴趣探索与该障碍相关的可能资源。这篇论文论证了与ADHD相关的注意力模式可以被理解为表达了一种替代的探究风格，或'探究式'风格，主要特征是变得好奇和参与探究的障碍更低，以及对与探究相关的认知和实践成本调节好奇的倾向更弱。从认识论角度探索这种探究式风格表明，它通常在认识论上是理性的，并且在重要方面可能是有利的。论文最后提出，可能有时使这种风格对ADHD个体不利的方面，往往会给他们所在的社会群体带来认识论上的好处。",
    },
    {
        "title": "Transient Frontal Fracturing: A Theoretical Account of Hyperfocus",
        "authors": "Derek M. Smith, et al.",
        "year": 2024,
        "venue": "Journal of Cognitive Neuroscience, 2024",
        "category": "【背景相关】超聚焦神经机制",
        "url": "https://watermark02.silverchair.com/jocn.a.2428.pdf",
        "spine": "超聚焦",
        "finding": "超聚焦源于前额叶控制层级的'断裂'：高级上下文信息不再能支配思维和行动的内容，中间层级信息脱耦合",
        "iso_claim": "许多人都经历过如此全神贯注于一项活动以至于失去对周围环境的意识、难以停止活动、时间知觉压缩的体验，这种体验通俗地称为超聚焦。基于报告的超聚焦现象学，作者提出这种体验通常源于前额叶控制层级的断裂，这降低了高级上下文信息支配思维和行动内容的能力。更准确地说，作者提出由上行唤醒系统变化带来的前额叶-纹状体-丘脑回路功能减弱，导致中间层级上下文信息（例如超聚焦的活动）与高级上下文的调节脱耦合。这一机制为理解LLM中类似的'超聚焦'现象（如重复、陷入循环、无法跳出局部上下文）提供了神经科学基础。",
    },
    {
        "title": "Artificial Neuropsychology: Are Large Language Models Developing Executive Functions?",
        "authors": "Hernan Ceferino Vazquez",
        "year": 2023,
        "venue": "arXiv:2305.04134, 2023",
        "category": "【背景相关】人工神经心理学",
        "url": "https://arxiv.org/pdf/2305.04134",
        "spine": "外部执行功能层",
        "finding": "使用经典神经心理学测试（河内塔）评估LLM的执行功能，发现规划和工作记忆能力有限但正在出现",
        "iso_claim": "AI快速发展，已经表现出执行广泛认知任务的能力，包括语言处理、视觉识别和决策。这一进展部分归功于LLM。大多数神经心理学家认为智能行为依赖于许多总体技能，即执行功能，它们依赖于额叶神经网络的正常运作，并开发了一系列测试来评估它们。这项工作提出了一个问题：LLM是否作为学习的一部分正在发展类似于人类的执行功能，并使用流行的河内塔方法评估GPT的规划功能和工作记忆。初步结果表明，LLM在河内塔相关任务中生成近最优解决方案，遵守任务约束，并表现出快速规划能力和高效的工作记忆使用，表明执行功能的潜在发展。然而，当任务不是已知的且不是训练数据的一部分时，这些能力相当有限，比训练有素的人类差。",
    },
]


def _abstract(p: dict) -> str:
    parts = [p["iso_claim"]]
    if p.get("finding"):
        parts.append(f"核心同构性发现：{p['finding']}")
    parts.append(
        f"作者：{p['authors']}（{p['year']}，{p['venue']}）。"
        f"分类：{p.get('category', '')}。该论文的同构落点在脊柱概念「{p['spine']}」。"
    )
    return " ".join(parts)


def _record(p: dict) -> dict:
    return {
        "id": p["url"],
        "title": p["title"],
        "abstract": _abstract(p),
        "year": p["year"],
        "venue": p["venue"],
        "doi": "",
        "url": p["url"],
        "cited_by": 0,
        "source": "isomorphism-curated",
        "domain": "isomorphism",
        "query": "ADHD LLM cognitive isomorphism",
        "authors": p["authors"],
        "spine": p["spine"],
        "category": p.get("category", ""),
        "iso_claim": p["iso_claim"],
        "finding": p.get("finding", ""),
    }


def save_seed(path: str = SEED_FILE) -> None:
    """把策展论文落盘为 academic 记录结构（committed，不依赖 99MB 大语料）。"""
    records = [_record(p) for p in ISOMORPHISM_PAPERS]
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def load_seed(path: str = SEED_FILE) -> list[dict]:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return [_record(p) for p in ISOMORPHISM_PAPERS]


def as_articles() -> list[dict]:
    """映射成「文章」结构（供知识萃取 / wiki 取材），标记为最高优先级同构证据。"""
    out = []
    for r in load_seed():
        title = r["title"]
        out.append({
            "title": title,
            "content": f"{title}. {r['abstract']}",
            "content_length": len(r["abstract"]),
            "url": r["url"],
            "source_title": r["venue"],
            "domain": "isomorphism",
            "year": r.get("year"),
            "is_academic": True,
            "is_isomorphism": True,
            "spine": r.get("spine", ""),
            "category": r.get("category", ""),
        })
    return out


if __name__ == "__main__":
    save_seed()
    print(f"已写入 {len(ISOMORPHISM_PAPERS)} 篇同构证据到 {SEED_FILE}")
