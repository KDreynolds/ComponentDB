/*
 * Copyright (c) UChicago Argonne, LLC. All rights reserved.
 * See LICENSE file.
 */
package gov.anl.aps.cdb.rest.entities;

/**
 *
 * @author djarosz
 */
public class NewControlRelationshipInformation {
    
    private int controlledMachineId; 
    private int controllingMachineId;     
    private Integer linkedParentMachineId = null; 
    private String controlInterfaceToParent; 

    public NewControlRelationshipInformation() {
    }

    public int getControlledMachineId() {
        return controlledMachineId;
    }

    public void setControlledMachineId(int controlledMachineId) {
        this.controlledMachineId = controlledMachineId;
    }

    public int getControllingMachineId() {
        return controllingMachineId;
    }

    public void setControllingMachineId(int controllingMachineId) {
        this.controllingMachineId = controllingMachineId;
    }

    public String getControlInterfaceToParent() {
        return controlInterfaceToParent;
    }

    public void setControlInterfaceToParent(String controlInterfaceToParent) {
        this.controlInterfaceToParent = controlInterfaceToParent;
    }    

    public Integer getLinkedParentMachineId() {
        return linkedParentMachineId;
    }

    public void setLinkedParentMachineId(Integer linkedParentMachineId) {
        this.linkedParentMachineId = linkedParentMachineId;
    }
          
}
