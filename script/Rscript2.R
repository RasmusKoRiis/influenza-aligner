
install.packages('plyr', repos = "http://cran.us.r-project.org")
install.packages("ggplot2", repos = "http://cran.us.r-project.org")
install.packages("gridExtra", repos = "http://cran.us.r-project.org")

library("gridExtra")
library(ggplot2)

startpath <- getwd()
directoryname = basename(startpath)


# NUMER OF MISMATCHES AND GAPS
csv_name <- list.files(pattern="primer*")
subfolder <- "/"
under_score <- "_"
plot_name <- "_primer_plot.pdf"
csv_file <- paste(startpath,subfolder,csv_name, sep="")
title <- "Total Primer Mismatch and Gaps for "


primer_check <- read.csv(file = csv_file)

filter_data <- primer_check[, c(1,2,16,18)]

filter_data$SequenceID = as.character(as.numeric(filter_data$SequenceID)) 

plot2 <- ggplot(data = filter_data, aes(Primer, SequenceID))+
  geom_tile(aes(fill = Total_Mis), color="white")

plot2 <- plot2 + 
  geom_text(aes(label = Length_Para), size = 3.1, color = "#F7F7FF") +
  scale_fill_gradient(          # adjust the fill color of the tiles
    low = "blue",
    high = "orange")+
  coord_equal(ratio = 0.5)+ 
  theme_minimal() + theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))+
  ggtitle(paste(title,directoryname,sep=""))

pdf_name <- paste(directoryname,plot_name, sep="")

pdf(file=pdf_name)
plot2
dev.off()


