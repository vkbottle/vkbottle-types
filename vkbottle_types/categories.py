from abc import ABC, abstractmethod
from vkbottle_types.methods import (
    account,
    ads,
    apps,
    appWidgets,
    auth,
    board,
    database,
    docs,
    downloadedGames,
    fave,
    friends,
    gifts,
    groups,
    leads,
    likes,
    market,
    messages,
    newsfeed,
    notes,
    notifications,
    orders,
    pages,
    photos,
    polls,
    prettyCards,
    search,
    secure,
    stats,
    status,
    storage,
    stories,
    streaming,
    users,
    utils,
    video,
    wall,
)
import typing

if typing.TYPE_CHECKING:
    from vkbottle import API


class APICategories(ABC):
    @property
    def account(self) -> account.AccountCategory:
        return account.AccountCategory(self.api_instance)

    @property
    def ads(self) -> ads.AdsCategory:
        return ads.AdsCategory(self.api_instance)

    @property
    def apps(self) -> apps.AppsCategory:
        return apps.AppsCategory(self.api_instance)

    @property
    def app_widgets(self) -> appWidgets.AppWidgetsCategory:
        return appWidgets.AppWidgetsCategory(self.api_instance)

    @property
    def auth(self) -> auth.AuthCategory:
        return auth.AuthCategory(self.api_instance)

    @property
    def board(self) -> board.BoardCategory:
        return board.BoardCategory(self.api_instance)

    @property
    def database(self) -> database.DatabaseCategory:
        return database.DatabaseCategory(self.api_instance)

    @property
    def docs(self) -> docs.DocsCategory:
        return docs.DocsCategory(self.api_instance)

    @property
    def downloaded_games(self) -> downloadedGames.DownloadedGamesCategory:
        return downloadedGames.DownloadedGamesCategory(self.api_instance)

    @property
    def fave(self) -> fave.FaveCategory:
        return fave.FaveCategory(self.api_instance)

    @property
    def friends(self) -> friends.FriendsCategory:
        return friends.FriendsCategory(self.api_instance)

    @property
    def gifts(self) -> gifts.GiftsCategory:
        return gifts.GiftsCategory(self.api_instance)

    @property
    def groups(self) -> groups.GroupsCategory:
        return groups.GroupsCategory(self.api_instance)

    @property
    def leads(self) -> leads.LeadsCategory:
        return leads.LeadsCategory(self.api_instance)

    @property
    def likes(self) -> likes.LikesCategory:
        return likes.LikesCategory(self.api_instance)

    @property
    def market(self) -> market.MarketCategory:
        return market.MarketCategory(self.api_instance)

    @property
    def messages(self) -> messages.MessagesCategory:
        return messages.MessagesCategory(self.api_instance)

    @property
    def newsfeed(self) -> newsfeed.NewsfeedCategory:
        return newsfeed.NewsfeedCategory(self.api_instance)

    @property
    def notes(self) -> notes.NotesCategory:
        return notes.NotesCategory(self.api_instance)

    @property
    def notifications(self) -> notifications.NotificationsCategory:
        return notifications.NotificationsCategory(self.api_instance)

    @property
    def orders(self) -> orders.OrdersCategory:
        return orders.OrdersCategory(self.api_instance)

    @property
    def pages(self) -> pages.PagesCategory:
        return pages.PagesCategory(self.api_instance)

    @property
    def photos(self) -> photos.PhotosCategory:
        return photos.PhotosCategory(self.api_instance)

    @property
    def polls(self) -> polls.PollsCategory:
        return polls.PollsCategory(self.api_instance)

    @property
    def prettyCards(self) -> prettyCards.PrettyCardsCategory:
        return prettyCards.PrettyCardsCategory(self.api_instance)

    @property
    def search(self) -> search.SearchCategory:
        return search.SearchCategory(self.api_instance)

    @property
    def secure(self) -> secure.SecureCategory:
        return secure.SecureCategory(self.api_instance)

    @property
    def stats(self) -> stats.StatsCategory:
        return stats.StatsCategory(self.api_instance)

    @property
    def status(self) -> status.StatusCategory:
        return status.StatusCategory(self.api_instance)

    @property
    def storage(self) -> storage.StorageCategory:
        return storage.StorageCategory(self.api_instance)

    @property
    def stories(self) -> stories.StoriesCategory:
        return stories.StoriesCategory(self.api_instance)

    @property
    def streaming(self) -> streaming.StreamingCategory:
        return streaming.StreamingCategory(self.api_instance)

    @property
    def users(self) -> users.UsersCategory:
        return users.UsersCategory(self.api_instance)

    @property
    def utils(self) -> utils.UtilsCategory:
        return utils.UtilsCategory(self.api_instance)

    @property
    def video(self) -> video.VideoCategory:
        return video.VideoCategory(self.api_instance)

    @property
    def wall(self) -> wall.WallCategory:
        return wall.WallCategory(self.api_instance)

    @property
    @abstractmethod
    def api_instance(self) -> "API":
        pass

    async def execute(self, code: str) -> typing.Any:
        return await self.api_instance.request("execute", {"code": code})
