from ..models.userModel import User


async def get_all_users():
    return await User.all()
