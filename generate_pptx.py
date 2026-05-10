#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate PPTX presentation for German Poetry AI-Assisted Translation Teaching
生成德语诗歌的 AI 辅助翻译教学 PPTX 演示文稿
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
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # 空白布局
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

def add_content_slide(prs, title, content_list, is_two_column=False):
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
    content_box = slide.shapes.add_textbox(Inches(1), Inches(1.8), Inches(8), Inches(5))
    text_frame = content_box.text_frame
    text_frame.word_wrap = True

    for i, content in enumerate(content_list):
        if i > 0:
            text_frame.add_paragraph()
        p = text_frame.paragraphs[i]
        p.text = content
        p.font.size = Pt(20)
        p.font.color.rgb = TEXT_COLOR
        p.space_before = Pt(12)
        p.space_after = Pt(12)
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
    title_p.font.size = Pt(40)
    title_p.font.bold = True
    title_p.font.color.rgb = PRIMARY_COLOR

    # 左栏
    left_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(4.5), Inches(5.5))
    left_frame = left_box.text_frame
    left_frame.word_wrap = True

    if left_title:
        left_frame.text = left_title
        left_p = left_frame.paragraphs[0]
        left_p.font.size = Pt(16)
        left_p.font.bold = True
        left_p.font.color.rgb = SECONDARY_COLOR
        left_frame.add_paragraph()

    for line in left_content:
        p = left_frame.add_paragraph()
        p.text = line
        p.font.size = Pt(16)
        p.font.color.rgb = TEXT_COLOR
        p.space_before = Pt(6)

    # 右栏
    right_box = slide.shapes.add_textbox(Inches(5), Inches(1.5), Inches(4.5), Inches(5.5))
    right_frame = right_box.text_frame
    right_frame.word_wrap = True

    if right_title:
        right_frame.text = right_title
        right_p = right_frame.paragraphs[0]
        right_p.font.size = Pt(16)
        right_p.font.bold = True
        right_p.font.color.rgb = SECONDARY_COLOR
        right_frame.add_paragraph()

    for line in right_content:
        p = right_frame.add_paragraph()
        p.text = line
        p.font.size = Pt(16)
        p.font.color.rgb = TEXT_COLOR
        p.space_before = Pt(6)

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
    "《流浪者夜歌》是歌德最著名的短篇诗歌之一，",
    "创作于 1776 年。",
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
    "AI 翻译初稿（DeepL）"
)

# Slide 7: AI 翻译的问题
add_content_slide(prs, "AI 翻译的问题分析", [
    "问题1：失去诗歌的音韵美",
    "原诗精妙的头韵（Gipfeln / Wipfeln）在中文中消失",
    "",
    "问题2：生硬的字面翻译",
    "「在所有山顶上有休息」明显不自然",
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
        "（有明显问题）"
    ],
    [
        "越过群山顶峰",
        "一片安宁",
        "林梢之上",
        "你感受不到",
        "哪怕一丝风声...",
        "",
        "（更优雅、更诗意）"
    ],
    "❌ AI 版本",
    "✓ 改进版本"
)

# Slide 9: 课堂流程 - 第一步
add_content_slide(prs, "课堂流程 | 第一步：体验 AI 翻译", [
    "▸ 学生用 ChatGPT/DeepL 翻译歌德《流浪者夜歌》",
    "",
    "▸ 展示 AI 生成的初稿",
    "",
    "⏱ 时间：3分钟"
])

# Slide 10: 课堂流程 - 第二步
add_content_slide(prs, "课堂流程 | 第二步：批判性分析", [
    "小组讨论分析：",
    "",
    "▸ 哪些地方翻得好？哪些不自然？",
    "",
    "▸ 原诗的意象和情感传达了吗？",
    "",
    "▸ 歌德想表达什么？（寻求宁静、生死观）",
    "",
    "⏱ 时间：8分钟"
])

# Slide 11: 课堂流程 - 第三、四步
add_content_slide(prs, "课堂流程 | 第三、四步", [
    "第三步：学生改进（8分钟）",
    "▸ 学生参考 AI 版本，结合对原诗的理解重新翻译",
    "▸ 小组互评、打磨",
    "",
    "第四步：规律总结（3分钟）",
    "▸ 诗歌翻译的关键技巧（音韵、意象、情感）",
    "▸ 这些策略对其他文体翻译的启发"
])

# Slide 12: 学生能获得什么
add_content_slide(prs, "学生能获得什么？", [
    "【翻译技能】诗歌意象转换、音韵节奏处理、文化内涵呈现",
    "",
    "【批判性思维】不盲目信任 AI、理解工具局限、人机协作价值",
    "",
    "【文化理解】德国古典文学、跨文化交流能力、诗学审美"
])

# Slide 13: 评价方式
add_content_slide(prs, "评价方式", [
    "① 能否指出 AI 的问题？← 理解深度",
    "",
    "② 改进版本比 AI 好吗？← 翻译水平",
    "",
    "③ 能否总结出翻译规律？← 迁移能力"
])

# Slide 14: 结束页
add_title_slide(prs,
    "感谢聆听",
    "德语诗歌 × AI = 创新翻译教学")

# 保存演示文稿
output_path = r"D:\my-ai-project\poetry-translation-teaching.pptx"
prs.save(output_path)
print("[OK] PPTX file generated successfully!")
print(f"[PATH] {output_path}")
print("[INFO] Total 14 slides")
print(f"[SIZE] {__import__('os').path.getsize(output_path) / 1024:.1f} KB")
