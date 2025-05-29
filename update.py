import win32com.client

def get_microsoft_updates():
    try:
        # Use COM to query the system for Microsoft updates
        update_session = win32com.client.Dispatch("Microsoft.Update.Session")
        update_searcher = update_session.CreateUpdateSearcher()
        
        # Search for all installed updates
        search_result = update_searcher.Search("IsInstalled=1")

        updates = []
        for update in search_result.Updates:
            updates.append({
                'Title': update.Title,
                'KBArticleIDs': ', '.join(update.KBArticleIDs),
                'InstalledOn': update.LastDeploymentChangeTime
            })

        return updates
    except Exception as e:
        print(f"Error retrieving Microsoft updates: {e}")
        return []
