package com.kob.backend.controller.Data;



import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.kob.backend.mapper.DataMapper;
import com.kob.backend.pojo.SportsData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
@CrossOrigin(origins = "http://localhost:8080") // 只允许从localhost:8080进行跨域请求

@RestController
public class DataController {
    @Autowired
    private DataMapper dataMapper;

    @GetMapping("/data")
    public List<SportsData> findLastFifteen() {
        QueryWrapper<SportsData> queryWrapper = new QueryWrapper<>();
        queryWrapper.orderByDesc("id").last("LIMIT 15");
        return dataMapper.selectList(queryWrapper);
    }
}