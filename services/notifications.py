from fastapi.encoders import jsonable_encoder
from repositories.notifications import NotificationRepository
from schemas.notifications import NotificationCreate


class NotificationService():
    def create_notification(notification_data: NotificationCreate):
        # Convert Pydantic model to dictionary
        notification_dict = jsonable_encoder(notification_data)

        # Insert notification into DB
        notification = NotificationRepository.create_notification(notification_dict)

        # Get the inserted notification from DB
        # result = NotificationRepository.get_notification(notification.inserted_id)

        print("Notification created successfully")
        return