
# def update_info(db: Session,status,info_id: int, info_update: schema.InfoBase):
#     db_info = db.query(models.Info).filter(models.Info.id == info_id).first()

#     if db_info is None:
#         return None  # Handle the case where the record is not found

#     # Update the fields you want to change
#     if info_update.date:
#         db_info.date = info_update.date
#     if info_update.project:
#         db_info.project = info_update.project
#     if info_update.task_id:
#         db_info.task_id = info_update.task_id
#     if info_update.task:
#         db_info.task = info_update.task
#     if status:
#         db_info.status = status
#     if info_update.start_time:
#         db_info.start_time = info_update.start_time
#     if info_update.end_time:
#         db_info.end_time = info_update.end_time
#     if info_update.duration:
#         db_info.duration = info_update.duration
#     if info_update.description:
#         db_info.description = info_update.description
#     if info_update.total_hours:
#         db_info.total_hours = info_update.total_hours

    # db.commit()
    # db.refresh(db_info)
    # return db_info
