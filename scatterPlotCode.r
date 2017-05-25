

spdata = read.csv("ScatterplotSCNdata.csv")

row,names(spdata) <- spdata$Gene
spdata <- spdata[,-1]

plot(row.names(spdata), spdata[,1], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='DPI', ylab='RQ value')
par(new=T)
plot(row.names(spdata), spdata[,2], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,3], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,4], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,5], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,6], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,7], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,8], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,9], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,10], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,11], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,12], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,13], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,14], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,15], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,16], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,17], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)
par(new=T)
plot(row.names(spdata), spdata[,18], pch=0, xlim=c(0.0,10.0), ylim=c(0.0,3.0), xlab='', ylab='', axes=F)