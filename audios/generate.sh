#!/bin/bash

# 德语音频内容
declare -a texts=(
    "Hallo mein Name ist Max"
    "Der Ball ist blau"
    "Ich habe zwei Geschwister"
    "Mein Lieblingsobst ist Orange"
    "Heute ist der fünfte"
    "Ich arbeite in einer Bank"
    "Letztes Jahr bin ich nach Frankreich gereist"
    "Mein Lieblingssport ist Fußball"
    "Dieses Kleid kostet fünfzig Euro"
    "Morgen wird es regnen"
    "Künstliche Intelligenz wird in der Medizin verwendet"
    "Der Klimawandel ist ein großes Problem"
    "Kultureller Austausch fördert Verständnis"
    "Der Professor empfiehlt praktisches Lernen"
    "Dreißig Minuten tägliche Bewegung sind empfohlen"
)

files=(
    "a1_01" "a1_02" "a1_03" "a1_04" "a1_05"
    "a2_01" "a2_02" "a2_03" "a2_04" "a2_05"
    "b1_01" "b1_02" "b1_03" "b1_04" "b1_05"
)

echo "生成德语音频文件..."

for i in "${!files[@]}"; do
    file="${files[$i]}"
    text="${texts[$i]}"
    espeak -v de -s 130 "$text" -w "${file}.wav" 2>/dev/null
    ffmpeg -i "${file}.wav" -q:a 9 -n "${file}.mp3" 2>/dev/null
    rm "${file}.wav"
    echo "✅ ${file}.mp3"
done

echo "完成！"
ls -lh *.mp3 | head -3
