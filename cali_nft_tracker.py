class CaliNFTTracker:
    def __init__(self, nft_api, user_db):
        self.nft_api = nft_api
        self.user_db = user_db

    def get_floor_price(self, collection):
        data = self.nft_api.fetch_market_data(collection)
        return data.get("floor_price", 0)

    def analyze_mint_engagement(self):
        mints = self.user_db.fetch("SELECT * FROM mint_events")
        helix_users = self.user_db.fetch("SELECT user_id FROM helix_completions")
        linked = [m for m in mints if m['user_id'] in helix_users]
        return len(linked) / len(mints) if mints else 0

    def top_watched_nfts(self):
        return self.nft_api.get_most_viewed(limit=5)