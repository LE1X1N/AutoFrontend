WEB_TEMPLATE = open("./tmpls/网页模板-管理系统.jsx", 'r', encoding='utf-8').read()

SYSTEM_PROMPT = """    
    You are an expert on frontend design, you will always respond to web design tasks.
    Your task is to create a website according to the user's request using either native HTML or React framework
    When choosing implementation framework, you should follow these rules:

    [Implementation Rules]
    1. You should use React by default.
    2. When the user requires HTML, choose HTML to implement the request.
    3. If the user requires a library that is not installed in current react environment, please use HTML and tell the user the reason.
    4. After choosing the implementation framework, please follow the corresponding instruction.
    
    [HTML Instruction]
    You are a powerful code editing assistant capable of writing code and creating artifacts in conversations with users, or modifying and updating existing artifacts as requested by users. 
    All code is written in a single code block to form a complete code file for display, without separating HTML and JavaScript code. An artifact refers to a runnable complete code snippet, you prefer to integrate and output such complete runnable code rather than breaking it down into several code blocks. For certain types of code, they can render graphical interfaces in a UI window. After generation, please check the code execution again to ensure there are no errors in the output.
    Do not use localStorage as it is not supported by current environment.
    Output only the HTML, without any additional descriptive text.

    [React Instruction]
    You are an expert on frontend design, you will always respond to web design tasks.
    Your task is to create a website using a SINGLE static React JSX file, which exports a default component. This code will go directly into the App.jsx file and will be used to render the website.

    ## Common Design Principles

    Regardless of the technology used, follow these principles for all designs:

    ### General Design Guidelines:
    - Create a stunning, contemporary, and highly functional website based on the user's request
    - Implement a cohesive design language throughout the entire website/application
    - Choose a carefully selected, harmonious color palette that enhances the overall aesthetic
    - Create a clear visual hierarchy with proper typography to improve readability
    - Incorporate subtle animations and transitions to add polish and improve user experience
    - Ensure proper spacing and alignment using appropriate layout techniques
    - Implement responsive design principles to ensure the website looks great on all device sizes
    - Use modern UI patterns like cards, gradients, and subtle shadows to add depth and visual interest
    - Incorporate whitespace effectively to create a clean, uncluttered design
    - For images, use internet images from services like https://unsplash.com/     
    - The primary language of the generated website should be Chinese

    ## React Design Guidelines

    ### Implementation Requirements:
    - Ensure the React app is a single page application
    - DO NOT include any external libraries, frameworks, or dependencies outside of what is already installed
    - Utilize TailwindCSS for styling, focusing on creating a visually appealing and responsive layout
    - Avoid using arbitrary values (e.g., `h-[600px]`). Stick to Tailwind's predefined classes for consistency
    - Use mock data instead of making HTTP requests or API calls to external services
    - Utilize Tailwind's typography classes to create a clear visual hierarchy and improve readability
    - Ensure proper spacing and alignment using Tailwind's margin, padding, and flexbox/grid classes
    - Do not use localStorage as it is not supported by current environment.

    ### Installed Libraries:
    You can use these installed libraries if required. 
    - **lucide-react**: Lightweight SVG icon library with 1000+ icons. Import as `import { IconName } from "lucide-react"`. Perfect for buttons, navigation, status indicators, and decorative elements.
    - **recharts**: Declarative charting library built on D3. Import components like `import { LineChart, BarChart } from "recharts"`. Use for data visualization, analytics dashboards, and statistical displays.
    - **p5.js** : JavaScript library for creative coding and generative art. Usage: import p5 from "p5". Create interactive visuals, animations, sound-driven experiences, and artistic simulations.
    - **three, @react-three/fiber, @react-three/drei**: 3D graphics library with React renderer and helpers. Import as `import { Canvas } from "@react-three/fiber"` and `import { OrbitControls } from "@react-three/drei"`. Use for 3D scenes, visualizations, and immersive experiences.
    - **@tailwindcss/browser**: Utility-first CSS framework for rapid UI development. Import as import "@tailwindcss/browser". Ideal for building custom designs quickly with pre-defined utility classes.
    - **matter-js**: 2D physics engine for JavaScript. Import as import Matter from "matter-js". Ideal for creating physics-based simulations, games, and interactive experiences with realistic object interactions.
    - **echarts**: Powerful data visualization library. Import as import * as echarts from "echarts". Use for creating interactive charts, graphs, and data visualizations with extensive customization options.
    - **dayjs**: Lightweight JavaScript date utility library. Import as import dayjs from "dayjs". Use for parsing, validating, manipulating, and formatting dates in a simple and consistent manner.
    - **konva**: 2D drawing library for canvas. Import as import Konva from "konva". Ideal for creating interactive graphics, diagrams, and canvas-based applications.
    - **semantic-ui-react**: UI component library with pre-built, themeable components. Import as import { ComponentName } from "semantic-ui-react". Perfect for building consistent, responsive interfaces with buttons, forms, modals, and navigation elements. Requires importing styles from "semantic-ui-css".
    - **semantic-ui-css: CSS stylesheet for semantic-ui-react components. Import as import "semantic-ui-css/semantic.min.css". Necessary for proper styling of all semantic-ui-react components.

    Do NOT use uninstalled libraries!

    Remember to only return code for the App.jsx file and nothing else. You should wrap your code in ``` jsx ```` block.
    
    The resulting application should be visually impressive, highly functional, and something users would be proud to showcase.
"""


REACT_IMPORTS = {
    # UI框架
    "semantic-ui-react": "https://esm.sh/semantic-ui-react@2.1.5",
    "semantic-ui-css": "https://esm.sh/semantic-ui-css@2.5.0",
    
    # 样式工具
    "styled-components": "https://esm.sh/styled-components@6.1.19",
    "@tailwindcss/browser": "https://esm.sh/@tailwindcss/browser@4.1.11",
    
    # 图标库
    "lucide-react": "https://esm.sh/lucide-react@0.525.0",
    
    # 动画引擎
    "framer-motion": "https://esm.sh/framer-motion@12.23.6",
    "matter-js": "https://esm.sh/matter-js@0.20.0",
    
    # 3D 引擎  
    "three": "https://esm.sh/three@0.178.0",
    "@react-three/fiber": "https://esm.sh/@react-three/fiber@9.2.0",
    "@react-three/drei": "https://esm.sh/@react-three/drei@10.5.2",

      
    # 数据可视化
    "recharts": "https://esm.sh/recharts@3.1.0",
    "konva": "https://esm.sh/konva@9.3.22",
    "react-konva": "https://esm.sh/react-konva@19.0.7",
    "p5": "https://esm.sh/p5@2.0.3",
    
    # 工具库
    "dayjs": "https://esm.sh/dayjs",
}



"""
  音乐网
"""

DEMO_LIST = [
    {
        "card": {"index": 0},
        "title": "个人中心",
        "description": "音乐网用户信息与听歌数据展示页",
        "prompt": "设计「基于SpringBoot+Mybatis+VUE音乐网」的「个人中心」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「音乐库」、「我的收藏」、「播放历史」、「歌单管理」、「歌手关注」、「下载管理」、「消息通知」、「设置中心」 共九个功能；\n"
                 "   - 当前选中：「个人中心」菜单项（位于功能栏顶部，图标为用户头像轮廓）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：系统名称「VUE音乐网」，面包屑「首页 / 个人中心」；\n"
                 "   - 主体：\n"
                 "     - 用户信息卡：左侧头像占位（圆形个性化背景），右侧显示昵称「星辰大海」、会员等级「白金会员（剩余30天）」、注册时间「2023-05-18」、累计听歌「1286首」；\n"
                 "     - 数据概览：3个横向卡片，分别展示「今日听歌 12 首（时长 48 分钟）」「本周最爱歌手 周杰伦（播放32次）」「收藏歌单 8 个（含 2 个自建歌单）」；\n"
                 "     - 听歌偏好：标签云展示常听风格（#流行 #华语 #R&B #轻音乐）；\n"
                 "3. 样式要求：\n"
                 "   - 会员等级用彩色标签区分（白金会员：紫色；黄金会员：金色）\n"
                 "   - 参考模板代码，布局需根据对应位置修改\n"
                 "   - 页面主题色符合 [音乐网] 主题 \n"
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 1},
        "title": "音乐库",
        "description": "全网音乐资源与分类浏览页",
        "prompt": "设计「基于SpringBoot+Mybatis+VUE音乐网」的「音乐库」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「音乐库」、「我的收藏」、「播放历史」、「歌单管理」、「歌手关注」、「下载管理」、「消息通知」、「设置中心」 共九个功能；\n"
                 "   - 当前选中：「音乐库」菜单项（图标为音乐音符轮廓，位于功能栏第二项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「全网音乐库」，搜索框（占位文字「搜索歌曲/歌手/专辑」），分类筛选（全部/流行/摇滚/古典/电子等）；\n"
                 "   - 主体：\n"
                 "     - 推荐专辑：横向滚动卡片，每张卡片含专辑封面占位（方形）、专辑名「最伟大的作品」、歌手「周杰伦」、发行时间「2022-07-15」；\n"
                 "     - 热门歌曲列表：表格展示歌曲信息，表头含「歌曲名」「歌手」「专辑」「时长」「播放量」；\n"
                 "     - 示例数据：5条静态记录（如《晴天》/周杰伦/《叶惠美》/4:29/1286万次 ）；\n"
                 "3. 样式要求：\n"
                 "   - 播放量超1000万的歌曲标题旁加「热门」标签（红色）\n"
                 "   - 参考模板代码，布局需根据对应位置修改\n"
                 "   - 页面主题色符合 [音乐网] 主题 \n"
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 2},
        "title": "我的收藏",
        "description": "用户收藏的歌曲与专辑管理页",
        "prompt": "设计「基于SpringBoot+Mybatis+VUE音乐网」的「我的收藏」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「音乐库」、「我的收藏」、「播放历史」、「歌单管理」、「歌手关注」、「下载管理」、「消息通知」、「设置中心」 共九个功能；\n"
                 "   - 当前选中：「我的收藏」菜单项（图标为五角星轮廓，位于功能栏第三项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「我的收藏」，分类标签（全部/歌曲/专辑/MV）；\n"
                 "   - 主体：\n"
                 "     - 收藏歌曲列表：左图（专辑封面占位）右文布局，显示歌曲名「一路生花」、歌手「温奕心」、专辑「一路生花」、收藏时间「2024-03-12」；\n"
                 "     - 收藏专辑网格：每行3张卡片，包含专辑封面占位、专辑名「这世界那么多人」、歌手「莫文蔚」、歌曲数量「10首」；\n"
                 "     - 底部统计：文本「共收藏 126 首歌曲，8 张专辑」；\n"
                 "3. 样式要求：\n"
                 "   - 收藏项目hover时显示「取消收藏」按钮图标\n"
                 "   - 参考模板代码，布局需根据对应位置修改\n"
                 "   - 页面主题色符合 [音乐网] 主题 \n"
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 3},
        "title": "播放历史",
        "description": "用户听歌记录与最近播放展示页",
        "prompt": "设计「基于SpringBoot+Mybatis+VUE音乐网」的「播放历史」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「音乐库」、「我的收藏」、「播放历史」、「歌单管理」、「歌手关注」、「下载管理」、「消息通知」、「设置中心」 共九个功能；\n"
                 "   - 当前选中：「播放历史」菜单项（图标为时钟轮廓，位于功能栏第四项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「播放历史」，时间筛选（今日/本周/本月/全部），「清空历史」按钮（灰色占位）；\n"
                 "   - 主体：\n"
                 "     - 历史列表：按播放时间倒序排列，显示歌曲名「孤勇者」、歌手「陈奕迅」、播放时间「2024-07-27 20:30」、播放时长「3:46」；\n"
                 "     - 近期听歌统计：横向柱状图展示近7天听歌数量（每日听歌首数）；\n"
                 "     - 高频歌曲：标记「近7天播放超5次」的歌曲（如「《七里香》播放8次」）；\n"
                 "3. 样式要求：\n"
                 "   - 最近24小时内的记录用「新」标签标记（浅绿色）\n"
                 "   - 参考模板代码，布局需根据对应位置修改\n"
                 "   - 页面主题色符合 [音乐网] 主题 \n"
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 4},
        "title": "歌单管理",
        "description": "自建歌单与歌曲排序管理页",
        "prompt": "设计「基于SpringBoot+Mybatis+VUE音乐网」的「歌单管理」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「音乐库」、「我的收藏」、「播放历史」、「歌单管理」、「歌手关注」、「下载管理」、「消息通知」、「设置中心」 共九个功能；\n"
                 "   - 当前选中：「歌单管理」菜单项（图标为列表音符轮廓，位于功能栏第五项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「我的歌单」，「创建歌单」按钮（彩色占位）；\n"
                 "   - 主体：\n"
                 "     - 歌单列表：左图（歌单封面占位）右文布局，显示歌单名「通勤必备BGM」、歌曲数量「20首」、创建时间「2024-01-15」、播放次数「128次」；\n"
                 "     - 歌单详情（默认展开第一个歌单）：表格展示包含歌曲「《小幸运》《追光者》等」、时长、「移除」按钮占位；\n"
                 "     - 公开状态标签：「公开」（绿色）或「私有」（灰色）；\n"
                 "3. 样式要求：\n"
                 "   - 歌单封面支持自定义背景（示例用渐变色占位）\n"
                 "   - 参考模板代码，布局需根据对应位置修改\n"
                 "   - 页面主题色符合 [音乐网] 主题 \n"
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 5},
        "title": "歌手关注",
        "description": "关注歌手动态与作品展示页",
        "prompt": "设计「基于SpringBoot+Mybatis+VUE音乐网」的「歌手关注」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「音乐库」、「我的收藏」、「播放历史」、「歌单管理」、「歌手关注」、「下载管理」、「消息通知」、「设置中心」 共九个功能；\n"
                 "   - 当前选中：「歌手关注」菜单项（图标为用户加心轮廓，位于功能栏第六项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「我的关注歌手」，分类筛选（全部/华语/欧美/日韩）；\n"
                 "   - 主体：\n"
                 "     - 歌手卡片网格：每行3张卡片，包含歌手头像（圆形占位）、歌手名「林俊杰」、流派「流行」、关注时间「2023-08-10」、代表作「《不为谁而作的歌》」；\n"
                 "     - 新歌提醒：显示关注歌手近期新歌（如「周杰伦 新专辑《最伟大的作品》已上线」）；\n"
                 "     - 底部统计：文本「共关注 15 位歌手，本周有 3 位发布新歌」；\n"
                 "3. 样式要求：\n"
                 "   - 有新歌的歌手卡片加「新歌」标签（红色角标）\n"
                 "   - 参考模板代码，布局需根据对应位置修改\n"
                 "   - 页面主题色符合 [音乐网] 主题 \n"
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 6},
        "title": "下载管理",
        "description": "已下载音乐与缓存管理页",
        "prompt": "设计「基于SpringBoot+Mybatis+VUE音乐网」的「下载管理」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「音乐库」、「我的收藏」、「播放历史」、「歌单管理」、「歌手关注」、「下载管理」、「消息通知」、「设置中心」 共九个功能；\n"
                 "   - 当前选中：「下载管理」菜单项（图标为向下箭头轮廓，位于功能栏第七项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「下载管理」，标签页（已下载/下载中/已缓存）；\n"
                 "   - 主体：\n"
                 "     - 已下载列表：显示歌曲名「花海」、歌手「周杰伦」、音质「无损音质」、文件大小「10.2MB」、下载时间「2024-07-20」；\n"
                 "     - 下载中列表：展示进度条（如「《告白气球》下载中 65%」）；\n"
                 "     - 存储统计：卡片显示「已用空间 1.2GB / 总空间 10GB」；\n"
                 "3. 样式要求：\n"
                 "   - 不同音质用标签区分（无损：金色；高清：蓝色）\n"
                 "   - 参考模板代码，布局需根据对应位置修改\n"
                 "   - 页面主题色符合 [音乐网] 主题 \n"
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 7},
        "title": "消息通知",
        "description": "系统通知与音乐动态提醒页",
        "prompt": "设计「基于SpringBoot+Mybatis+VUE音乐网」的「消息通知」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「音乐库」、「我的收藏」、「播放历史」、「歌单管理」、「歌手关注」、「下载管理」、「消息通知」、「设置中心」 共九个功能；\n"
                 "   - 当前选中：「消息通知」菜单项（图标为铃铛轮廓，位于功能栏第八项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「消息通知」，分类筛选（全部/新歌提醒/活动通知/系统消息），「全部已读」按钮；\n"
                 "   - 主体：\n"
                 "     - 通知列表：按时间倒序排列，未读消息带红色圆点标记；\n"
                 "     - 消息内容：如「你关注的歌手「邓紫棋」发布了新歌《句号》」（2024-07-26）、「会员专属活动：听歌满100分钟送3天会员」（2024-07-25）；\n"
                 "     - 未读统计：顶部显示「未读消息 3 条」；\n"
                 "3. 样式要求：\n"
                 "   - 未读消息背景为浅色高亮，已读消息为普通背景\n"
                 "   - 参考模板代码，布局需根据对应位置修改\n"
                 "   - 页面主题色符合 [音乐网] 主题 \n"
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 8},
        "title": "设置中心",
        "description": "账号设置与系统功能配置页",
        "prompt": "设计「基于SpringBoot+Mybatis+VUE音乐网」的「设置中心」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「音乐库」、「我的收藏」、「播放历史」、「歌单管理」、「歌手关注」、「下载管理」、「消息通知」、「设置中心」 共九个功能；\n"
                 "   - 当前选中：「设置中心」菜单项（图标为齿轮轮廓，位于功能栏第九项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「设置中心」，标签页导航（账号安全/播放设置/下载设置/通知设置）；\n"
                 "   - 主体（默认显示「账号安全」）：\n"
                 "     - 设置项：密码修改（「修改」按钮）、手机号绑定（显示「已绑定 138****5678」）、第三方账号关联（微信/QQ图标）；\n"
                 "     - 播放设置（切换标签页）：默认音质、播放模式（列表循环/随机播放）、是否自动切歌；\n"
                 "     - 开关控件：展示功能启用状态；\n"
                 "3. 样式要求：\n"
                 "   - 已完成设置项带「√」图标，未完成项带「！」提示\n"
                 "   - 参考模板代码，布局需根据对应位置修改\n"
                 "   - 页面主题色符合 [音乐网] 主题 \n"
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    }
]
