package com.density.controller;

import com.density.service.WaterLevelService;
import com.density.util.WaterDetails;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class TrackerController {

    @Autowired
    WaterLevelService waterLevelService;

    public TrackerController(WaterLevelService waterLevelService) {
        this.waterLevelService = waterLevelService;
    }

    //getCurrentValue
//setCurrentConsumption

    @GetMapping(value = "/getCurrentWaterLevel/{nodeId}")

    public ResponseEntity getCurrentWaterLevel(@RequestParam String nodeId){
        return waterLevelService.getWaterLevel(nodeId);

    }

    @PostMapping(value = "/updateWaterStatus")
    public WaterDetails setWaterLevel(@RequestBody WaterDetails waterDetails){
        return waterLevelService.setWaterLevel(waterDetails);
    }
}
