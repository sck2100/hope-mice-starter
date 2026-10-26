# 換了任何一章的 mouse.png 或 reveal.png 之後跑一次：python tools/sync-chapters.py
# 1. 把每一章的 mouse.png 複製到「每一章」的 assets/friends/chN.png（好朋友小老鼠，每章要能獨立運作所以各放一份）
# 2. 重跑每一章的 tools/make-export-data.py（下載用的 base64 圖）
import pathlib, shutil, subprocess, sys

root = pathlib.Path(__file__).resolve().parent.parent
chapters = sorted(root.glob('chapter*-*'), key=lambda d: int(d.name[7:].split('-')[0]))
for d in chapters:
    friends = d / 'assets' / 'friends'
    friends.mkdir(exist_ok=True)
    for src in chapters:
        n = src.name[7:].split('-')[0]
        shutil.copyfile(src / 'assets' / 'mouse.png', friends / f'ch{n}.png')
    subprocess.run([sys.executable, str(d / 'tools' / 'make-export-data.py')], check=True)
print('done:', ', '.join(d.name for d in chapters))
