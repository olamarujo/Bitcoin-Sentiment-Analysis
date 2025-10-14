###############################################################################################################################################################################
# (INDICATORS)
# (MA,STD, Z-SCORE)
def indicator(df, to_calculate, timeframe, weighter=False):

    # if to weight is not needed
    if not weighter:
        ma =  df[to_calculate].rolling(window=timeframe).mean() # moving average
        std = df[to_calculate].rolling(window=timeframe).std() # standad deviation
   
    # if needs to me weighted by something
    else:
        ma = (df[to_calculate] * df[weighter]).rolling(window=timeframe).sum() / df[weighter].rolling(window=timeframe).sum() # moving average
        
        std = ((((df[to_calculate]** 2) * df[weighter]).rolling(window=timeframe).sum() / df[weighter].rolling(window=timeframe).sum()) - (ma ** 2)) ** 0.5 # standard deviation
    
    ma = ma.shift(-1)
    std = std.shift(-1)
        
        
    z_score = (df[to_calculate] - ma) / std # z-score
    
    # create a new dataframe with just the datetime    
    df_new = df[['datetime']].copy()

    # add the indicators to new columns     
    df_new[f'{to_calculate}_{timeframe}_ma'] = ma
    df_new[f'{to_calculate}_{timeframe}_std'] = std
    df_new[f'{to_calculate}_{timeframe}_z_score'] = z_score
    
    # return the result
    return df_new
#####################
# (CORRELATION)
def correlation(df, correlator_1, correlator_2, timeframe):

        correlation = df[correlator_1].rolling(window=timeframe).corr(df.correlator_2)
        return correlation

 #####################  
# (BOLINGER BANDS)
def band(df, to_calculate, timeframe, band_range = [2,4] , interval = 1, weighter=False):
        # if to weight is not needed
    if not weighter:
        ma =  df[to_calculate].rolling(window=timeframe).mean() # moving average
        std = df[to_calculate].rolling(window=timeframe).std() # standad deviation

    # if needs to me weighted by something
    else:
        ma = (
            (df[to_calculate] * df[weighter]).rolling(window=timeframe).sum() / # moving average
            df[weighter].rolling(window=timeframe).sum()
        )
        std = (
            (((df[to_calculate]** 2) * df[weighter]).rolling(window=timeframe).sum() / # standad deviation
             df[weighter].rolling(window=timeframe).sum()) - (ma ** 2)) ** 0.5
        
    # create a new dataframe with just the datetime    
    df_new = df[['datetime']].copy()


    # calculate the band and insert into a new column
    for band in range(band_range[0], band_range[1] + 1, interval):
        df_new[f'{to_calculate}_{timeframe}_{band}_upper'] = ma + band * std
        df_new[f'{to_calculate}_{timeframe}_{band}_lower'] = ma - band * std
  
    # return the result
    return df_new 

###############################################################################################################################################################################