from .base import APIModel

class LinkDetail(APIModel):
    """通过链接获取作品详情的模型"""
    text: str  # 包含分享链接的字符串