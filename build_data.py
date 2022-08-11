import pandas as pd
import json

def build_data():
    
    with open('inventory_response_1.json') as f:
        data = json.load(f)
    
    inventory_df = pd.DataFrame(data['rows'])

    event_df = inventory_df['event'].apply(pd.Series)

    event_venue_df = event_df['venue'].apply(pd.Series)

    event_df.columns = ["event_" + col 
                        for col in event_df.columns]
    event_venue_df.columns = ["event_venue_" + col 
                                for col in event_venue_df.columns]

    df = pd.concat([inventory_df, event_df, event_venue_df], axis=1 )

    return df