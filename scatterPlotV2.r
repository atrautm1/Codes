

spddata = read.csv("ScatterplotSCNdataSD.csv", header=TRUE, sep=",")

attach(spddata)

svg("Scatterplot.svg")

par(mfrow=c(3,3))
plot(X, S.PAL.1.1, main= 'PAL 1.1', xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=0, xlab='DPI', ylab='Fold Change', xaxt='n', col="gold4")
lines(X, S.PAL.1.1, col="gold4")
axis(1, at=seq(0,8, length=9))
arrows(X, S.PAL.1.1, x1=X, y1=S.PAL.1.1+SDS.PAL.1.1, length=0.05, angle=90, code=3, col="gold4")
par(new=T)
plot(X, R.PAL.1.1, xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=2, xlab='', ylab='', axes=F, col="gold")
lines(X, R.PAL.1.1, col="gold")
arrows(X, R.PAL.1.1, x1=X, y1=R.PAL.1.1+SDR.PAL.1.1, length=0.05, angle=90, code=3, col="gold")

plot(X, S.PAL.2, main= 'PAL 2', xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=0, xlab='DPI', ylab='Fold Change', xaxt='n', col="gold4")
lines(X, S.PAL.2, col="gold4")
axis(1, at=seq(0,8, length=9))
arrows(X, S.PAL.2, x1=X, y1=S.PAL.2+SDS.PAL.2, length=0.05, angle=90, code=3, col="gold4")
par(new=T)
plot(X, R.PAL.2, xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=2, xlab='', ylab='', axes=F, col="gold")
lines(X, R.PAL.2, col="gold")
arrows(X, R.PAL.2, x1=X, y1=R.PAL.2+SDR.PAL.2, length=0.05, angle=90, code=3, col="gold")

plot(X, S.PAL.1.3, main= 'PAL 1.2', xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=0, xlab='DPI', ylab='Fold Change', xaxt='n', col="gold4")
lines(X, S.PAL.1.3, col="gold4")
axis(1, at=seq(0,8, length=9))
arrows(X, S.PAL.1.3, x1=X, y1=S.PAL.1.3+SDS.PAL.1.3, length=0.05, angle=90, code=3, col="gold4")
par(new=T)
plot(X, R.PAL.1.3, xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=2, xlab='', ylab='', axes=F, col="gold")
lines(X, R.PAL.1.3, col="gold")
arrows(X, R.PAL.1.3, x1=X, y1=R.PAL.1.3+SDR.PAL.1.3, length=0.05, angle=90, code=3, col="gold")

plot(X, S.IFS.1, main= 'IFS 1', xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=0, xlab='DPI', ylab='Fold Change', xaxt='n', col="gold4")
lines(X, S.IFS.1, col="gold4")
axis(1, at=seq(0,8, length=9))
arrows(X, S.IFS.1, x1=X, y1=S.IFS.1+SDS.IFS.1, length=0.05, angle=90, code=3, col="gold4")
par(new=T)
plot(X, R.IFS.1, xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=2, xlab='', ylab='', axes=F, col="gold")
lines(X, R.IFS.1, col="gold")
arrows(X, R.IFS.1, x1=X, y1=R.IFS.1+SDR.IFS.1, length=0.05, angle=90, code=3, col="gold")

plot(X, S.IFS.2, main= 'IFS 2', xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=0, xlab='DPI', ylab='Fold Change', xaxt='n', col="gold4")
lines(X, S.IFS.2, col="gold4")
axis(1, at=seq(0,8, length=9))
arrows(X, S.IFS.2, x1=X, y1=S.IFS.2+SDS.IFS.2, length=0.05, angle=90, code=3, col="gold4")
par(new=T)
plot(X, R.IFS.2, xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=2, xlab='', ylab='', axes=F, col="gold")
lines(X, R.IFS.2, col="gold")
arrows(X, R.IFS.2, x1=X, y1=R.IFS.2+SDR.IFS.2, length=0.05, angle=90, code=3, col="gold")

plot(X, S.GmIFR, main= 'GmIFR', xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=0, xlab='DPI', ylab='Fold Change', xaxt='n', col="gold4")
lines(X, S.GmIFR, col="gold4")
axis(1, at=seq(0,8, length=9))
arrows(X, S.GmIFR, x1=X, y1=S.GmIFR+SDS.GmIFR, length=0.05, angle=90, code=3, col="gold4")
par(new=T)
plot(X, R.GmIFR, xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=2, xlab='', ylab='', axes=F, col="gold")
lines(X, R.GmIFR, col="gold")
arrows(X, R.GmIFR, x1=X, y1=R.GmIFR+SDR.GmIFR, length=0.05, angle=90, code=3, col="gold")

plot(X, S.NADPH.IFR, main= 'NADPH-IFR', xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=0, xlab='DPI', ylab='Fold Change', xaxt='n', col="gold4")
lines(X, S.NADPH.IFR, col="gold4")
axis(1, at=seq(0,8, length=9))
arrows(X, S.NADPH.IFR, x1=X, y1=S.NADPH.IFR+SDS.NADPH.IFR, length=0.05, angle=90, code=3, col="gold4")
par(new=T)
plot(X, R.NADPH.IFR, xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=2, xlab='', ylab='', axes=F, col="gold")
lines(X, R.NADPH.IFR, col="gold")
arrows(X, R.NADPH.IFR, x1=X, y1=R.NADPH.IFR+SDR.NADPH.IFR, length=0.05, angle=90, code=3, col="gold")

plot(X, S.CHS.7, main= 'CHS 7', xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=0, xlab='DPI', ylab='Fold Change', xaxt='n', col="gold4")
lines(X, S.CHS.7, col="gold4")
axis(1, at=seq(0,8, length=9))
arrows(X, S.CHS.7, x1=X, y1=S.CHS.7+SDS.CHS.7, length=0.05, angle=90, code=3, col="gold4")
par(new=T)
plot(X, R.CHS.7, xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=2, xlab='', ylab='', axes=F, col="gold")
lines(X, R.CHS.7, col="gold")
arrows(X, R.CHS.7, x1=X, y1=R.CHS.7+SDR.CHS.7, length=0.05, angle=90, code=3, col="gold")

plot(X, S.CHS.8, main= 'CHS 8', xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=0, xlab='DPI', ylab='Fold Change', xaxt='n', col="gold4")
lines(X, S.CHS.8, col="gold4")
axis(1, at=seq(0,8, length=9))
arrows(X, S.CHS.8, x1=X, y1=S.CHS.8+SDS.CHS.8, length=0.05, angle=90, code=3, col="gold4")
par(new=T)
plot(X, R.CHS.8, xlim=c(0.0,8.0), ylim=c(0.0,5.0), pch=2, xlab='', ylab='', axes=F, col="gold")
lines(X, R.CHS.8, col="gold")
arrows(X, R.CHS.8, x1=X, y1=R.CHS.8+SDR.CHS.8, length=0.05, angle=90, code=3, col="gold")

dev.off()