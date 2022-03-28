from bot import InternetSpeedTwitterBot
import os

PROMISED_DOWN = os.environ["PROMISED_DOWN"]
PROMISED_UP = os.environ["PROMISED_UP"]
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
USERNAME = os.environ["USERNAME"]


def main():
    twitter_bot = InternetSpeedTwitterBot()
    up_speed, down_speed = twitter_bot.get_internet_speed()
    tweet = compose_tweet(PROMISED_UP, PROMISED_DOWN, up_speed, down_speed)
    twitter_bot.tweet_at_provider(TWITTER_PASSWORD, TWITTER_EMAIL, USERNAME, tweet)


def compose_tweet(prom_up, prom_down, up_spd, down_spd):
    if float(prom_up) > float(up_spd) or float(prom_down) > float(down_spd):
        tweet = f"Hey Internet Provider, why is my internet speed {up_spd}up/{down_spd}down " \
                f"when I pay for {prom_up}up/{prom_down}down?"
        return tweet
    else:
        tweet = f"Wow! My Internet provider is doing alright! I pay for {prom_up}up/{prom_down}down, " \
                f"and I'm actually getting {up_spd}up/{down_spd}down!"
        return tweet


if __name__ == '__main__':
    main()
