# -*- mode: python -*-

block_cipher = None
a = Analysis(['gui_integration.py'],
         pathex=['D:\\MY Works\\New folder\\TMS\\TMS\\'],
          binaries=[],
         datas=[
         ("C:\\Users\Moham\\AppData\Local\\Programs\\Python\\Python39\Lib\\site-packages\\branca\\*.json","branca"),
         ("C:\\Users\Moham\\AppData\Local\\Programs\\Python\\Python39\Lib\\site-packages\\branca\\templates","templates"),
         ("C:\\Users\Moham\\AppData\Local\\Programs\\Python\\Python39\Lib\\site-packages\\folium\\templates","templates"),
         ],
         hiddenimports=[],
         hookspath=[],
         runtime_hooks=[],
         excludes=[],
         win_no_prefer_redirects=False,
         win_private_assemblies=False,
         cipher=block_cipher,
         noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      [],
      name='TMS_2020',
      debug=False,
      bootloader_ignore_signals=False,
      strip=False,
      upx=True,
      runtime_tmpdir=None,
      console=False )