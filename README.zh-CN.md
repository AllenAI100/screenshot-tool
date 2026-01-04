# 🖼️ Screenshot Tool - 网页截图工具

一个强大的全网页截图工具，支持网站和 HTML 文件，完美处理滚动动画和响应式设计。

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-orange.svg)

[English](README.md) | 简体中文

## ✨ 特性

- 🌐 **截取网站** - 截取任意在线网站
- 📄 **本地文件** - 无需服务器即可截取 HTML 文件
- 🎭 **动画支持** - 完美处理滚动触发的动画
- 📱 **响应式** - 支持桌面、平板和移动端视口
- ⏱️ **可定制** - 可自定义等待时间以适应慢速网站
- 🎯 **自动检测** - 自动识别 URL 或本地文件
- 🚀 **快速** - 高效的无头浏览器截图
- 💎 **高质量** - 无损 PNG 输出

## 📦 安装

### 前置要求

- Python 3.6 或更高版本
- pip（Python 包管理器）

### 安装依赖

```bash
# 安装 Playwright
pip3 install playwright

# 安装 Chromium 浏览器
playwright install chromium
```

就这样！你可以开始截图了。

## 🚀 快速开始

### 基本用法

```bash
# 截取网站（自动生成文件名）
python3 capture_web.py https://example.com

# 指定输出文件名
python3 capture_web.py https://example.com my-screenshot.png

# 桌面视图（1920px 宽）
python3 capture_web.py https://github.com github.png 1920

# 移动端视图（390px 宽）
python3 capture_web.py https://github.com github-mobile.png 390
```

### 高级用法

```bash
# 慢加载网站（等待 10 秒）
python3 capture_web.py https://heavy-site.com output.png 1920 10

# 本地 HTML 文件
python3 capture_web.py design.html design-screenshot.png

# 平板视图
python3 capture_web.py https://example.com tablet.png 1024

# 更大的移动设备
python3 capture_web.py https://example.com mobile-large.png 414
```

## 📖 使用示例

### 示例 1：截取竞争对手网站

```bash
python3 capture_web.py https://competitor.com
# 输出: competitor_com_screenshot.png
```

### 示例 2：移动端预览

```bash
python3 capture_web.py https://mysite.com mobile-preview.png 390
```

### 示例 3：设计灵感

```bash
python3 capture_web.py https://dribbble.com dribbble.png 1920
```

### 示例 4：慢加载网站

```bash
python3 capture_web.py https://react-app.com output.png 1920 15
```

### 示例 5：本地设计稿

```bash
python3 capture_web.py my-design.html design.png
```

## 🐍 Python API

```python
from capture_web import capture_screenshot

# 基本用法
capture_screenshot('https://example.com')

# 带参数
capture_screenshot(
    source='https://example.com',
    output_path='screenshot.png',
    width=1920,
    wait_time=3
)

# 移动端视图
capture_screenshot(
    source='https://example.com',
    output_path='mobile.png',
    width=390,
    wait_time=5
)

# 本地文件
capture_screenshot('design.html', 'design.png')
```

## 📐 视口尺寸

| 设备 | 宽度 | 使用场景 |
|------|------|----------|
| 桌面（完整） | 1920px | 标准桌面显示器 |
| 桌面（笔记本） | 1440px | 笔记本电脑 |
| 平板 | 1024px | iPad 和平板设备 |
| 移动端（iPhone） | 390px | iPhone 12/13/14 |
| 移动端（大屏） | 414px | iPhone Plus/Max 机型 |

## 🔧 工作原理

本工具解决了一个常见问题：现代网站使用滚动触发动画，元素默认是隐藏的。标准截图工具会遗漏这些元素。

**解决方案：**

1. **加载页面** - 在无头浏览器中打开 URL 或文件
2. **等待** - 允许 JavaScript 和资源加载
3. **滚动** - 缓慢滚动整个页面以触发动画
4. **强制显示** - 注入 CSS 确保所有元素可见
5. **截图** - 生成全网页截图
6. **保存** - 输出高质量 PNG

这确保截图中的**每个元素**都可见。

## 💡 使用技巧

### 对于慢速网站

如果网站加载时间很长：

```bash
python3 capture_web.py https://slow-site.com output.png 1920 10
#                                                                    ↑
#                                                            等待 10 秒
```

### 对于重度 JavaScript 网站

SPA、React 应用、Vue 应用通常需要更多时间：

```bash
python3 capture_web.py https://react-app.com output.png 1920 15
```

### 对于懒加载网站

工具通过滚动整个页面自动处理懒加载图片和内容。

### 对于被屏蔽的内容

某些网站会屏蔽无头浏览器（Cloudflare 等）：

**解决方案：** 在浏览器中保存页面（Cmd+S / Ctrl+S），然后：

```bash
python3 capture_web.py saved-page.html screenshot.png
```

### 对于需要登录的页面

工具不支持认证。替代方案：

1. 在浏览器中登录网站
2. 将页面保存为 HTML（Cmd+S）
3. 截取保存的 HTML 文件

## 🐛 故障排除

### 问题："Page load had issues"

**不严重！** 截图仍会被捕获。尝试：
- 增加等待时间：`python3 capture_web.py URL output.png 1920 10`
- 检查网站是否在浏览器中正常加载

### 问题：截图是空白的

网站可能屏蔽了无头浏览器：
- 大幅增加等待时间
- 将页面保存为 HTML 并截取文件

### 问题：元素缺失

增加滚动延迟：
1. 编辑 `capture_web.py`
2. 找到 `time.sleep(0.05)`
3. 改为 `time.sleep(0.1)` 或 `time.sleep(0.15)`

### 问题：超时错误

网站太慢或被屏蔽：
- 增加等待时间到 10-15 秒
- 检查网站在浏览器中是否正常加载
- 使用本地 HTML 文件方法

### 问题：图片未加载

增加等待时间让图片加载：

```bash
python3 capture_web.py URL output.png 1920 8
```

## 📊 输出

- **格式**: PNG（无损质量）
- **大小**: 完整页面通常 1-5MB
- **尺寸**: 匹配实际页面大小（非视口）
- **命名**: 从 URL 自动生成或可自定义

## 🔒 隐私与安全

- **无追踪**: 不向外部服务器发送数据
- **本地处理**: 所有操作在你的机器上运行
- **无云服务**: 截图保存在本地
- **开源**: 代码完全透明

## 📝 系统要求

```
Python >= 3.6
playwright >= 1.40.0
Chromium 浏览器（Playwright 自动安装）
```

## 📄 许可证

MIT License - 详见 [LICENSE.txt](LICENSE.txt)

## 🤝 贡献

欢迎贡献！请：

1. Fork 本仓库
2. 创建特性分支
3. 进行更改
4. 提交 Pull Request

## 📞 支持

如有问题、疑问或建议：

- 在 GitHub 上提 issue
- 检查现有 issue 寻找解决方案
- 阅读上方的故障排除指南

## 🎯 使用场景

- **竞品分析** - 存档竞争对手网站
- **设计灵感** - 从 Dribbble、Behance 等网站保存设计
- **文档制作** - 创建可视化文档
- **演示文稿** - 在演示文稿中包含网站截图
- **响应式测试** - 比较移动端与桌面端布局
- **回归测试** - 比较修改前后的截图
- **存档** - 在网站更改前保存网页
- **客户工作** - 与客户分享网站模型

## 🗺️ 开发路线图

- [ ] 添加 PDF 导出选项
- [ ] 支持认证
- [ ] 批量截图模式
- [ ] Web UI 界面
- [ ] Docker 支持
- [ ] CI/CD 集成

## ⭐ Star 本项目

如果你觉得这个工具有用，请在 GitHub 上 star 它！

---

**用 ❤️ 为 web 开发社区制作**

## 🙏 致谢

感谢所有使用和贡献这个工具的开发者！

特别感谢：
- Playwright 团队的出色工具
- 所有贡献者和反馈者
- 开源社区

## 📚 相关资源

- [Playwright 文档](https://playwright.dev/python/)
- [GitHub 仓库](https://github.com/AllenAI100/screenshot-tool)
- [问题反馈](https://github.com/AllenAI100/screenshot-tool/issues)
