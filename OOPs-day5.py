class InstagramAccount:
    
    # Constructor
    def __init__(self, account_name, password):
        # Public
        self.account_name = account_name
        
        # Protected
        self._private_reels = []
        
        # Private
        self.__archived_reels = []
        self.__password = password

    # 1. Add private reel
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    # 2. Display private reels
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    # 3. Add archived reel
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    # 4. Display archived reels
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    # 5. Getter for archived reels
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"

    # 6. Setter to update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Wrong old password!")


# ========================
# Task Implementation
# ========================

# Create object
account = InstagramAccount("john_doe", "1234")

# Add private reels
account.add_private_reel("Trip Reel")
account.add_private_reel("Family Reel")

# Add archived reels
account.add_archived_reel("Old Memories")
account.add_archived_reel("College Days")

# Display private reels
print("\nFollower View:")
account.display_private_reels(True)

print("\nNon-Follower View:")
account.display_private_reels(False)

# Display archived reels
print("\nCorrect Password:")
account.display_archived_reels("1234")

print("\nWrong Password:")
account.display_archived_reels("0000")

# Update password
print("\nUpdating Password:")
account.set_password("1234", "5678")

# Check again with new password
print("\nCheck with New Password:")
account.display_archived_reels("5678")