#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
德语听力练习平台 - 音频生成脚本
自动生成15个德语MP3音频文件
"""

import os
import sys
import io
from pathlib import Path

# 设置UTF-8编码
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def generate_audios():
    """使用gTTS生成德语音频文件"""

    try:
        from gtts import gTTS
    except ImportError:
        print("❌ gTTS未安装，正在安装...")
        os.system(f"{sys.executable} -m pip install gtts -q")
        from gtts import gTTS

    # 设置输出目录
    audio_dir = Path(__file__).parent / "audios"
    audio_dir.mkdir(exist_ok=True)
    os.chdir(audio_dir)

    # 定义所有音频内容
    exercises = {
        # A1级 - 基础级
        "a1_01.mp3": {
            "text": "Hallo, mein Name ist Max.",
            "level": "A1",
            "title": "问候"
        },
        "a1_02.mp3": {
            "text": "Der Ball ist blau.",
            "level": "A1",
            "title": "颜色"
        },
        "a1_03.mp3": {
            "text": "Ich habe zwei Geschwister.",
            "level": "A1",
            "title": "家庭"
        },
        "a1_04.mp3": {
            "text": "Mein Lieblingsobst ist Orange.",
            "level": "A1",
            "title": "食物"
        },
        "a1_05.mp3": {
            "text": "Heute ist der fünfte.",
            "level": "A1",
            "title": "数字"
        },

        # A2级 - 初级+
        "a2_01.mp3": {
            "text": "Ich arbeite in einer Bank.",
            "level": "A2",
            "title": "工作"
        },
        "a2_02.mp3": {
            "text": "Letztes Jahr bin ich nach Frankreich gereist.",
            "level": "A2",
            "title": "旅行"
        },
        "a2_03.mp3": {
            "text": "Mein Lieblingssport ist Fußball.",
            "level": "A2",
            "title": "爱好"
        },
        "a2_04.mp3": {
            "text": "Dieses Kleid kostet fünfzig Euro.",
            "level": "A2",
            "title": "购物"
        },
        "a2_05.mp3": {
            "text": "Morgen wird es regnen.",
            "level": "A2",
            "title": "天气"
        },

        # B1级 - 中级
        "b1_01.mp3": {
            "text": "Künstliche Intelligenz wird hauptsächlich in der medizinischen Diagnose verwendet.",
            "level": "B1",
            "title": "现代技术"
        },
        "b1_02.mp3": {
            "text": "Der Klimawandel ist ein globales Problem für unsere Welt.",
            "level": "B1",
            "title": "环境问题"
        },
        "b1_03.mp3": {
            "text": "Kultureller Austausch fördert gegenseitiges Verständnis zwischen Menschen.",
            "level": "B1",
            "title": "文化交流"
        },
        "b1_04.mp3": {
            "text": "Der Professor empfiehlt mehr praktische Aktivitäten im Unterricht.",
            "level": "B1",
            "title": "教育改革"
        },
        "b1_05.mp3": {
            "text": "Der Arzt rät zu mindestens dreißig Minuten moderater Bewegung täglich.",
            "level": "B1",
            "title": "健康生活"
        },
    }

    print("🎵 开始生成德语音频文件...")
    print(f"📁 输出目录: {audio_dir}")
    print("=" * 50)
    print()

    success_count = 0
    error_count = 0

    for filename, data in exercises.items():
        try:
            text = data["text"]
            level = data["level"]
            title = data["title"]

            print(f"⏳ 生成 [{level}] {title}...")

            # 创建gTTS对象 - 使用德语和较慢的语速
            tts = gTTS(
                text=text,
                lang='de',
                slow=False,
                lang_check=False
            )

            # 保存文件
            tts.save(filename)

            # 获取文件大小
            file_size = os.path.getsize(filename)
            size_kb = file_size / 1024

            print(f"   ✅ {filename} ({size_kb:.1f}KB)")
            success_count += 1

        except Exception as e:
            print(f"   ❌ {filename} - 错误: {str(e)}")
            error_count += 1

    print()
    print("=" * 50)
    print(f"✅ 成功生成: {success_count}/15")
    if error_count > 0:
        print(f"❌ 失败: {error_count}/15")

    # 统计信息
    print()
    print("📊 文件统计:")
    a1_files = [f for f in os.listdir() if f.startswith('a1_')]
    a2_files = [f for f in os.listdir() if f.startswith('a2_')]
    b1_files = [f for f in os.listdir() if f.startswith('b1_')]

    print(f"   A1级: {len(a1_files)}/5 文件")
    print(f"   A2级: {len(a2_files)}/5 文件")
    print(f"   B1级: {len(b1_files)}/5 文件")

    total_size = sum(os.path.getsize(f) for f in os.listdir() if f.endswith('.mp3'))
    print(f"   总大小: {total_size / (1024*1024):.2f}MB")

    if success_count == 15:
        print()
        print("🎉 所有音频生成完成！")
        print()
        print("📱 下一步:")
        print("   1. 刷新浏览器 (http://localhost:3000)")
        print("   2. 点击'学生练习'")
        print("   3. 选择难度等级")
        print("   4. 点击音频播放按钮测试")
        return True
    else:
        print()
        print("⚠️  部分文件生成失败，请检查网络连接")
        return False

if __name__ == "__main__":
    try:
        success = generate_audios()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏹️  用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        sys.exit(1)
