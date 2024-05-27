package com.kob.backend.pojo;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;
@Data
@AllArgsConstructor
@NoArgsConstructor
@TableName("data1")

public class SportsData {
    private Integer id;

    private Float accx;
    private Float accy;
    private Float accz;
    private Float temp;
    private LocalDateTime recordedat;
    private Float asx;
    private Float asy;
    private Float asz;
    private Float angx;
    private Float angy;
    private Float angz;
   // private Float bmp;
}
