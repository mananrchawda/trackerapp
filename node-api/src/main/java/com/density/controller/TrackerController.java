package com.density.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class TrackerController {


//getCurrentValue
//setCurrentConsumption

    @GetMapping(value = "/getCurrentWaterLevel/{nodeId}")
    public ResponseEntity getCurrentWaterLevel(@RequestParam String nodeId){
       return null;
    }

}
