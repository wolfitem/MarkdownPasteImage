# MarkdownPasteImage
- 一个sublime text 3 的插件
- 支持直接将粘贴板中的图片，生成图片文件，并输出markdown语法的图片链接

查看演示视频：

http://v.youku.com/v_show/id_XMzE0ODExMjM4OA==.html

## 安装

#### Windows:
复制 `MarkdownPasteImage\src\sublime-plug\Packages`目录到 `%appdata%\Sublime Text 3\Packages`目录 

复制 `Clipboarad2img.exe`到 C盘根目录 

#### Mac:
复制 `MarkdownPasteImage\src\sublime-plug\Packages`目录到 `%appdata%\Sublime Text 3\Packages`目录 

安装工具 
```
brew install pngpaste
```

## 使用

#### Windows:
- 使用任何工具截取一个图片到粘贴板
- 在sublime text 3 的 md文档中，使用快捷键  `ctrl` + `shift` + `alt` + `v` . 直接输出 图片链接

#### Mac:
- 使用任何工具截取一个图片到粘贴板
- 在sublime text 3 的 md文档中，使用快捷键   `command` + `shift` + `v` . 直接输出 图片链接

## 配置 
- 修改  `%appdata%\Sublime Text 3\Packages\User\markdown_paste_image.sublime-settings` 文件
- markdown_paste_image.sublime-settings 文件中相关的配置说明