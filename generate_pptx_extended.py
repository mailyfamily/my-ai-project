#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extended PPTX with translation standards and multiple translator versions
包含翻译标准和多家翻译家版本的扩展 PPTX
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor

# 定义颜色方案
PRIMARY_COLOR = RGBColor(0, 102, 204)  # 蓝色
SECONDARY_COLOR = RGBColor(0, 61, 153)  # 深蓝
ACCENT_COLOR = RGBColor(255, 107, 107)  # 红色
TEXT_COLOR = RGBColor(51, 51, 51)  # 深灰
WHITE = RGBColor(255, 255, 255)
LIGHT_BG = RGBColor(249, 249, 249)

# 创建演示文稿
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

def add_title_slide(prs, title, subtitle=""):
    """添加标题幻灯片"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = SECONDARY_COLOR

    # 添加顶部装饰线
    top_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.15))
    top_shape.fill.solid()
    top_shape.fill.fore_color.rgb = PRIMARY_COLOR
    top_shape.line.color.rgb = PRIMARY_COLOR

    # 标题
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_frame.word_wrap = True
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(54)
    title_p.font.bold = True
    title_p.font.color.rgb = WHITE
    title_p.alignment = PP_ALIGN.CENTER

    # 副标题
    if subtitle:
        subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(1))
        subtitle_frame = subtitle_box.text_frame
        subtitle_frame.text = subtitle
        subtitle_p = subtitle_frame.paragraphs[0]
        subtitle_p.font.size = Pt(28)
        subtitle_p.font.color.rgb = WHITE
        subtitle_p.alignment = PP_ALIGN.CENTER

    # 作者信息
    author_box = slide.shapes.add_textbox(Inches(0.5), Inches(5.8), Inches(9), Inches(0.8))
    author_frame = author_box.text_frame
    author_frame.text = "翻译课教师 | 5分钟说课演示"
    author_p = author_frame.paragraphs[0]
    author_p.font.size = Pt(18)
    author_p.font.color.rgb = WHITE
    author_p.alignment = PP_ALIGN.CENTER

def add_content_slide(prs, title, content_list):
    """添加内容幻灯片"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE

    # 添加顶部装饰线
    top_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.2))
    top_shape.fill.solid()
    top_shape.fill.fore_color.rgb = PRIMARY_COLOR
    top_shape.line.color.rgb = PRIMARY_COLOR

    # 标题
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(8.4), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = PRIMARY_COLOR

    # 添加标题下方的横线
    line_shape = slide.shapes.add_shape(1, Inches(0.8), Inches(1.35), Inches(8.4), Inches(0.05))
    line_shape.fill.solid()
    line_shape.fill.fore_color.rgb = SECONDARY_COLOR
    line_shape.line.color.rgb = SECONDARY_COLOR

    # 内容
    content_box = slide.shapes.add_textbox(Inches(1), Inches(1.8), Inches(8), Inches(5.2))
    text_frame = content_box.text_frame
    text_frame.word_wrap = True

    for i, content in enumerate(content_list):
        if i > 0:
            text_frame.add_paragraph()
        p = text_frame.paragraphs[i]
        p.text = content
        p.font.size = Pt(18)
        p.font.color.rgb = TEXT_COLOR
        p.space_before = Pt(8)
        p.space_after = Pt(8)
        p.level = 0

def add_two_column_slide(prs, title, left_content, right_content, left_title="", right_title=""):
    """添加两栏对比幻灯片"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE

    # 顶部装饰线
    top_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.2))
    top_shape.fill.solid()
    top_shape.fill.fore_color.rgb = PRIMARY_COLOR
    top_shape.line.color.rgb = PRIMARY_COLOR

    # 标题
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(8.4), Inches(0.7))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_p = title_frame.paragraphs[0]
    title_p.font.size = Pt(36)
    title_p.font.bold = True
    title_p.font.color.rgb = PRIMARY_COLOR

    # 左栏
    left_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(4.5), Inches(5.5))
    left_frame = left_box.text_frame
    left_frame.word_wrap = True

    if left_title:
        left_frame.text = left_title
        left_p = left_frame.paragraphs[0]
        left_p.font.size = Pt(14)
        left_p.font.bold = True
        left_p.font.color.rgb = SECONDARY_COLOR
        left_frame.add_paragraph()

    for line in left_content:
        p = left_frame.add_paragraph()
        p.text = line
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_COLOR
        p.space_before = Pt(4)

    # 右栏
    right_box = slide.shapes.add_textbox(Inches(5), Inches(1.5), Inches(4.5), Inches(5.5))
    right_frame = right_box.text_frame
    right_frame.word_wrap = True

    if right_title:
        right_frame.text = right_title
        right_p = right_frame.paragraphs[0]
        right_p.font.size = Pt(14)
        right_p.font.bold = True
        right_p.font.color.rgb = SECONDARY_COLOR
        right_frame.add_paragraph()

    for line in right_content:
        p = right_frame.add_paragraph()
        p.text = line
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_COLOR
        p.space_before = Pt(4)

# ========== 生成幻灯片 ==========

# Slide 1: 标题页
add_title_slide(prs,
    "德语诗歌的 AI 辅助翻译教学",
    "以歌德《流浪者夜歌》为案例")

# Slide 2: 教学理念
add_content_slide(prs, "教学理念", [
    "在 AI 时代，翻译课不是教学生「怎样做得和 AI 一样」，",
    "而是教学生「怎样做得比 AI 更好」。",
    "",
    "诗歌是最好的试金石，因为它最能暴露 AI 的局限，",
    "也最能激发学生的创意。"
])

# Slide 3: 为什么选择诗歌+AI
add_content_slide(prs, "为什么选择诗歌+AI？", [
    "▸ 诗歌翻译最具挑战性——意象、韵律、文化内涵",
    "",
    "▸ AI 在诗歌上容易失败——无法理解比喻、破坏音韵",
    "",
    "▸ 这正好是教学的黄金切口——暴露问题而激发思考"
])

# Slide 4: 教学方法
add_content_slide(prs, "教学方法", [
    "让学生用 AI 翻译德语诗歌初稿，然后：",
    "",
    "① 指出 AI 的错误 ← 理解诗歌深层含义",
    "",
    "② 分析为什么出错 ← 学会翻译规律",
    "",
    "③ 人工优化 ← 掌握翻译技巧"
])

# Slide 5: 案例介绍
add_content_slide(prs, "案例：歌德《流浪者夜歌》", [
    "Johann Wolfgang von Goethe (1749-1832)",
    "",
    "《流浪者夜歌》是歌德最著名的短篇诗歌之一，创作于 1776 年。",
    "",
    "这首诗以其独特的意象和宁静致远的意蕴，",
    "是理解诗歌翻译难点的完美教材。"
])

# Slide 6: 原诗 vs AI 初稿
add_two_column_slide(prs,
    "原诗 vs AI 初稿",
    [
        "Über allen Gipfeln",
        "Ist Ruh,",
        "In allen Wipfeln",
        "Spürest du",
        "Kaum einen Hauch;",
        "Die Vögelein schweigen im Wald.",
        "Warte nur, balde",
        "Ruhest du auch."
    ],
    [
        "在所有山顶上",
        "有休息，",
        "在所有树冠中",
        "你可以感觉到",
        "几乎没有微风；",
        "森林里的小鸟沉默不语。",
        "等等，很快",
        "你也会休息。"
    ],
    "德文原诗",
    "AI 翻译初稿"
)

# Slide 7: AI 翻译的问题
add_content_slide(prs, "AI 翻译的问题分析", [
    "问题1：失去诗歌的音韵美",
    "原诗头韵（Gipfeln / Wipfeln）在中文消失",
    "",
    "问题2：生硬的字面翻译",
    "「在所有山顶上有休息」不自然，应该「山顶上一片宁静」",
    "",
    "问题3：未能传达情感意蕴",
    "原诗的宁静致远、生死顿悟的哲思被消解"
])

# Slide 8: 学生改进版本
add_two_column_slide(prs,
    "学生改进版本（示例）",
    [
        "在所有山顶上",
        "有休息...",
        "森林里的小鸟沉默不语。",
        "",
        "（AI 版本，有问题）"
    ],
    [
        "越过群山顶峰",
        "一片安宁",
        "林梢之上",
        "你感受不到",
        "哪怕一丝风声...",
        "",
        "（改进版本，更优）"
    ],
    "❌ AI 版本",
    "✓ 改进版本"
)

# ===== NEW: 翻译家版本对比 =====

# Slide 9: 历代翻译家的版本
add_content_slide(prs, "历代翻译家的诠释", [
    "同一首诗，不同翻译家有不同的理解和表现方式。",
    "这正是翻译教学的核心：展现翻译的多元性。",
    "",
    "我们来看看中国翻译大家是如何处理这首诗的。"
])

# Slide 10: 钱钟书版本
add_content_slide(prs, "钱钟书版本（直译+意译兼备）", [
    "山顶上都静寂无声，",
    "树顶间你难觉有微风；",
    "林中小鸟无声地呆着，",
    "等一下，不久你也会安眠。",
    "",
    "钱钟书追求「准确」和「自然」的平衡，",
    "既忠于原义，又考虑汉语表达习惯。"
])

# Slide 11: 郭沫若版本
add_content_slide(prs, "郭沫若版本（追求音韵和意象）", [
    "山顶暮晖尽消散，",
    "树梢微风隐约传，",
    "林间百鸟已沉眠，",
    "待我一朝亦长眠。",
    "",
    "郭沫若着重诗的「音乐性」，",
    "力求用中文的对仗、平仄来再现原诗的音韵美。"
])

# Slide 12: 翻译标准的三个维度
add_content_slide(prs, "翻译标准：信达雅", [
    "【信】— 准确传达原文内容和意思",
    "不曲解、不遗漏、准确理解原作",
    "",
    "【达】— 用地道的汉语表达，读起来自然流畅",
    "避免生硬直译，符合中文表达习惯",
    "",
    "【雅】— 重现原作的文学性、美感和意蕴",
    "考虑音韵、意象、情感等审美层面"
])

# Slide 13: AI vs 人工翻译的本质区别
add_content_slide(prs, "AI vs 人工翻译的本质区别", [
    "AI 的优势：",
    "▸ 快速、准确、一致（在基础翻译层面）",
    "",
    "AI 的局限：",
    "▸ 难以理解隐喻、意象、文化内涵",
    "▸ 不能实现「信达雅」三者的统一",
    "▸ 无法进行创意的、个性化的诠释"
])

# Slide 14: 最佳翻译的三个原则
add_content_slide(prs, "实现最佳翻译的三原则", [
    "1. 深度理解阶段",
    "   透彻理解原文的字面意、深层意、情感意",
    "",
    "2. 创意转换阶段",
    "   在保留核心内涵的基础上，用目标语言的独特表现方式",
    "",
    "3. 打磨与反思阶段",
    "   对比多个版本，进行反复修改和优化"
])

# Slide 15: 课堂流程 - 第一步
add_content_slide(prs, "课堂流程 | 第一步：体验 AI 翻译", [
    "▸ 学生用 ChatGPT/DeepL 翻译歌德《流浪者夜歌》",
    "",
    "▸ 展示 AI 生成的初稿",
    "",
    "⏱ 时间：3分钟"
])

# Slide 16: 课堂流程 - 第二步
add_content_slide(prs, "课堂流程 | 第二步：批判性分析", [
    "小组讨论分析：",
    "",
    "▸ 哪些地方翻得好？哪些不自然？",
    "",
    "▸ 对标历代翻译家的版本，AI 缺少了什么？",
    "",
    "▸ 原诗的「信达雅」在 AI 版本中体现了多少？"
])

# Slide 17: 课堂流程 - 第三、四步
add_content_slide(prs, "课堂流程 | 第三、四步", [
    "第三步：学生改进（8分钟）",
    "▸ 学生参考 AI、钱钟书、郭沫若等版本",
    "▸ 以「信达雅」为目标重新翻译",
    "▸ 小组互评、打磨",
    "",
    "第四步：规律总结（3分钟）",
    "▸ 反思自己的翻译决策",
    "▸ 理解翻译的多元化和标准化的辩证关系"
])

# Slide 18: 学生能获得什么
add_content_slide(prs, "学生能获得什么？", [
    "【翻译技能】信达雅的实践、多版本对标、打磨能力",
    "",
    "【批判性思维】理解 AI 的角色和限制、评估翻译质量",
    "",
    "【文化理解】古典诗歌、中西审美差异、翻译文化"
])

# Slide 19: 评价方式
add_content_slide(prs, "评价方式", [
    "① 能否指出 AI 的问题？← 理解深度",
    "",
    "② 改进版本在「信达雅」上的改进 ← 翻译水平",
    "",
    "③ 能否反思翻译决策的原因？← 迁移能力"
])

# Slide 20: 核心价值
add_content_slide(prs, "教学的核心价值", [
    "这个方法的本质是：",
    "",
    "用 AI 的局限来突显人的价值",
    "用历代大师的案例来启蒙学生的创意",
    "",
    "让学生既学会了翻译技术，",
    "也理解了翻译艺术。"
])

# Slide 21: 结束页
add_title_slide(prs,
    "感谢聆听",
    "德语诗歌 × AI × 翻译标准 = 创新教学")

# 保存演示文稿
output_path = r"D:\my-ai-project\poetry-translation-teaching-extended.pptx"
prs.save(output_path)
print("[OK] Extended PPTX file generated successfully!")
print(f"[PATH] {output_path}")
print("[INFO] Total 21 slides (extended version)")
print(f"[SIZE] {__import__('os').path.getsize(output_path) / 1024:.1f} KB")
