from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler
import json

API_KEY = "5815583689:AAEHQxXoLxMpmd-qAxm7k78tshxZEsNK_BA"

x = open('ip_config.txt', 'r')
xy = x.read()
y = json.loads(xy)


class StartMessage(BaseMessage):
    """Start menu, create all app sub-menus."""

    LABEL = "start"

    def __init__(self, navigation: NavigationHandler) -> None:
        """Init StartMessage class."""
        super().__init__(navigation, StartMessage.LABEL)
        second_menu = RaspberryPIselectionmenu(navigation)
        self.add_button(label="Server Selection", callback=second_menu)

    def update(self) -> str:
        """Update message content."""
        return "Hello, world!"
      
class RaspberryPIselectionmenu(BaseMessage):
    """Second menu, create an inlined button."""

    LABEL = "action"

    def __init__(self, navigation: NavigationHandler) -> None:
        """Init SecondMenuMessage class."""
        super().__init__(navigation, StartMessage.LABEL, inlined=True)

        # 'run_and_notify' function executes an action and return a string as Telegram notification.
        self.add_button(label="Action", callback=self.run_and_notify)
        # 'back' button goes back to previous menu
        self.add_button_back()
        # 'home' button goes back to main menu
        self.add_button_home()

    def update(self) -> str:
        """Update message content."""
        # emoji can be inserted with a keyword enclosed with ::
        # list of emojis can be found at this link: https://www.webfx.com/tools/emoji-cheat-sheet/
        return ":warning: Second message"

    @staticmethod
    def run_and_notify() -> str:
           """Update message content."""
           return "This is a notification"

TelegramMenuSession(API_KEY).start(StartMessage)