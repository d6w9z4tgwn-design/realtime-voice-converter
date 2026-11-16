# realtime-voice-converter

マイク入力をリアルタイムにリング変調する音声エフェクト。AI声質変換・ピッチ変換ではない。

Real-time microphone ring modulation effect, not AI voice cloning or pitch shifting.

## Setup / 起動
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## Usage / 使用例
`python app.py --frequency 80 --mix 0.8` — headphones required to avoid feedback; live audio hardware untested.

Python 3.10+ recommended. AI-generated development assistance was used.
