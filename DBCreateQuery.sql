DROP TABLE IF EXISTS Reading;
CREATE TABLE [Reading] (
	[reportId] INTEGER PRIMARY KEY,
	[timestmp] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 	
    [ph1] NVARCHAR(50)  NULL,  
	[temp1] NVARCHAR(50)  NULL, 
	[ph2] NVARCHAR(50)  NULL,
	[temp2] NVARCHAR(50)  NULL, 
	[mAo1_25] NVARCHAR(50)  NULL,
	[mAo1_26] NVARCHAR(50)  NULL,
	[mAo1_27] NVARCHAR(50)  NULL,
	[mAo1_28] NVARCHAR(50)  NULL,
	[mAo1_29] NVARCHAR(50)  NULL,
	[mAo2_25] NVARCHAR(50)  NULL,
	[mAo2_26] NVARCHAR(50)  NULL,
	[mAo2_27] NVARCHAR(50)  NULL,
	[mAo2_28] NVARCHAR(50)  NULL,
	[mAo2_29] NVARCHAR(50)  NULL,
	[relay1_16] NVARCHAR(50)  NULL,
	[relay1_17] NVARCHAR(50)  NULL,
	[relay1_18] NVARCHAR(50)  NULL,
	[relay1_19] NVARCHAR(50)  NULL,
	[relay1_20] NVARCHAR(50)  NULL,
	[relay1_21] NVARCHAR(50)  NULL,
	[relay1_22] NVARCHAR(50)  NULL,
	[relay1_23] NVARCHAR(50)  NULL,
	[relay2_16] NVARCHAR(50)  NULL,
	[relay2_17] NVARCHAR(50)  NULL,
	[relay2_18] NVARCHAR(50)  NULL,
	[relay2_19] NVARCHAR(50)  NULL,
	[relay2_20] NVARCHAR(50)  NULL,
	[relay2_21] NVARCHAR(50)  NULL,
	[relay2_22] NVARCHAR(50)  NULL,
	[relay2_23] NVARCHAR(50)  NULL,
	[relay3_16] NVARCHAR(50)  NULL,
	[relay3_17] NVARCHAR(50)  NULL,
	[relay3_18] NVARCHAR(50)  NULL,
	[relay3_19] NVARCHAR(50)  NULL,
	[relay3_20] NVARCHAR(50)  NULL,
	[relay3_21] NVARCHAR(50)  NULL,
	[relay3_22] NVARCHAR(50)  NULL,
	[relay3_23] NVARCHAR(50)  NULL
); 	