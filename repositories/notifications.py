from config.database import notifications_collection

class NotificationRepository():
    def create_notification(notification: dict):
        return notifications_collection.insert_one(notification)
    
    def get_all_notifications():
        return notifications_collection.find()