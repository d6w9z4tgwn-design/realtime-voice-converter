# Realtime Voice Converter

マイク入力へリング変調をかけ、リアルタイムに変化した音声を出力する実験的なオーディオエフェクトです。声のクローンやAI変換ではなく、信号処理の基本を体験するためのアプリです。

## 主な機能

- 低遅延のマイク入力・出力ストリーム
- 変調周波数と原音/エフェクトのミックス量を指定
- 位相を維持した連続処理により、ブロックごとの不自然な切れ目を軽減

## セットアップ
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## 使い方

`python app.py --frequency 80 --mix 0.8` を実行します。`frequency` は変調周波数（Hz）、`mix` はエフェクト量（0〜1）です。フィードバック防止のため必ずヘッドホンを使用してください。

Python 3.10+ 推奨。ライブ音声の動作は、使用するオーディオ機器で確認してください。
