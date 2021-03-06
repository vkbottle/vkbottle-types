from typing import Optional

from vkbottle_types.responses import downloadedGames
from .base_category import BaseCategory


class DownloadedGamesCategory(BaseCategory):
    async def get_paid_status(
        self, user_id: Optional[int] = None, **kwargs
    ) -> downloadedGames.PaidStatusResponseModel:
        """downloadedGames.getPaidStatus method
        :param user_id:
        """

        params = self.get_set_params(locals())
        return downloadedGames.PaidStatusResponse(
            **await self.api.request("downloadedGames.getPaidStatus", params)
        ).response
