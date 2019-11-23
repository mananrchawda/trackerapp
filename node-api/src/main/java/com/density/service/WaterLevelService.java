package com.density.service;


import com.density.util.WaterDetails;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class WaterLevelService {

    public WaterDetails waterDetails;


    public ResponseEntity getWaterLevel(String nodeId) {
        return null;
    }

    public WaterDetails setWaterLevel(WaterDetails waterDetails) {
        waterDetails.setNodeId(waterDetails.getNodeId());
        waterDetails.setWaterCapacity(waterDetails.getWaterCapacity());
        //Will insert into MongoDB against nodeId
        return waterDetails;
    }
}
