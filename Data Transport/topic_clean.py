from google.cloud import pubsub_v1

project_id = "dataengineeringproject-456307"
topic_id = "MyTopic-sub"

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()
topic_path = publisher.topic_path(project_id, topic_id)

for subscription in subscriber.list_subscriptions(project=project_id):
    if subscription.topic == topic_path:
        subscriber.delete_subscription(subscription.name)
        print(f"Deleted subscription: {subscription.name}")
