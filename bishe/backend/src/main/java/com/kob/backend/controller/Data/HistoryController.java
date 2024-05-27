package com.kob.backend.controller.Data;

import com.kob.backend.mapper.HistoryMapper;
import com.kob.backend.pojo.SportsData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

@CrossOrigin(origins = "http://localhost:8080") // 只允许从localhost:8080进行跨域请求
@RestController
public class HistoryController {
    @Autowired
    private HistoryMapper historyMapper;
    @GetMapping("/history")
    public List<SportsData> getDataBetween(@RequestParam String start, @RequestParam String end){
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        LocalDateTime startDate = LocalDateTime.parse(start,formatter);
        LocalDateTime endDate = LocalDateTime.parse(end,formatter);
        return historyMapper.findByRecordedAtBetween(startDate,endDate);
    }
}
