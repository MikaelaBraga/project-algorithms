def study_schedule(permanence_period, target_time):
    try:
        online_users = 0

        for login, logout in permanence_period:
            if login <= target_time <= logout:
                online_users += 1

        return online_users
    except TypeError:
        return None
