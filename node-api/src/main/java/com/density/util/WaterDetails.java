package com.density.util;

public class WaterDetails {

    private String nodeId;
    private String waterCapacity;

    public WaterDetails(String nodeId, String waterCapacity) {
        this.nodeId = nodeId;
        this.waterCapacity = waterCapacity;
    }

    public String getNodeId() {
        return nodeId;
    }

    public void setNodeId(String nodeId) {
        this.nodeId = nodeId;
    }

    public String getWaterCapacity() {
        return waterCapacity;
    }

    public void setWaterCapacity(String waterCapacity) {
        this.waterCapacity = waterCapacity;
    }
}

