package com.kob.backend.mapper;
import com.kob.backend.pojo.SportsData;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.time.LocalDateTime;
import java.util.List;

@Mapper
public interface HistoryMapper {

    @Select("SELECT * FROM data1 WHERE recordedat BETWEEN #{start} AND #{end}")
    List<SportsData> findByRecordedAtBetween(@Param("start") LocalDateTime start, @Param("end") LocalDateTime end);
}
