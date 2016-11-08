library(twitteR)

requestURL <- 'https://api.twitter.com/oauth/request_token'
accessURL <- 'https://api.twitter.com/oauth/access_token'
authURL <- 'https://api.twitter.com/oauth/authorize'
consumerKey <- #consumer key here
consumerSecret <- #consumer secret here
cred <- OAuthFactory$new(consumerKey=consumerKey,
                        consumerSecret=consumerSecret,
                        requestURL=requestURL,
                        accessURL=accessURL,
                        authURL=authURL)
cred$handshake()
registerTwitterOAuth(cred)
setwd('/Users/matthewcooper/R workspace')
points <- read.table('PhilippinesPoints.txt',header=T,sep=',')
coords <- paste(points$latitude,points$longitude,sep=',')

alltweets <- NULL
alltweets <- data.frame(alltweets)

for (i in coords[1:length(coords)]){
  results <- NULL
  index <- which(coords==i,arr.ind=TRUE)
  Sys.sleep(9)
  if (length(which(alltweets$location==i,arr.ind=TRUE))<10){
    try(results <- searchTwitter(searchString='', n=1000, geocode=paste(i,'10mi',sep=','), retryOnRateLimit=10))
  }
  print(paste(toString(index),toString(index/length(coords)*100),'percent complete'))
  if (length(results)>0){
    resultsdf <- twListToDF(results)
    resultsdf$location <- index
    alltweets <- rbind(alltweets,resultsdf)
  }
  if (index%%20==0){
    print(paste(dim(alltweets)[1],'tweets collected,',dim(alltweets[!is.na(alltweets$latitude),])[1],'tweets georeferenced'))
  }
}

alltweets <- alltweets[!is.na(alltweets$latitude),]

#create delimitter so python can recognize new lines, since \n doesn't seem to be working. My delimitter will be 'shrooby'
alltweets$shrooby <- as.character('$hr0oby')
alltweets$newtext <- paste(alltweets$shrooby, alltweets$text)

write.table(alltweets$newtext, 'alltweetstext2.txt', row.names=FALSE, sep='\t', fileEncoding='UTF-8')
write.table(alltweets$longitude, 'alltweetslong2.txt', row.names=FALSE, sep='\t')
write.table(alltweets$latitude, 'alltweetslat2.txt', row.names=FALSE, sep='\t')

results <- searchTwitter(searchString='Robert DeLong', n=100)
resultsdf <- twListToDF(results)
resultsdf$text
