/*
 * Copyright (c) UChicago Argonne, LLC. All rights reserved.
 * See LICENSE file.
 */
package gov.anl.aps.cdb.portal.view.objects;

import gov.anl.aps.cdb.portal.controllers.ItemDomainMachineDesignController;
import gov.anl.aps.cdb.portal.model.db.entities.Item;
import gov.anl.aps.cdb.portal.model.db.entities.ItemElement;
import java.io.Serializable;
import org.primefaces.event.FlowEvent;
import org.primefaces.model.TreeNode;

/**
 * This class is intended to be used by another controller class, e.g.,
 * ItemDomainMachineDesignController, and is utilized when adding a new cable
 * design item.
 * 
 * I have not added annotations for the named bean or scope since it's not
 * envisioned to be used that way, and I'm not sure if they'd cause problems by
 * being present.
 * 
 * @author cmcchesney
 */
public class ItemDomainCableDesignWizard implements Serializable {

    private ItemDomainCableDesignWizardClient client;
    private TreeNode machineDesignTree = null;
    private String name = "";
    private TreeNode endpoint1 = null;
    private TreeNode selectedEndpoint = null;
    private String cableType = "";
    private Item selectedCableCatalogItem = null;

    /**
     * Creates new instance with a "dummy" client implementation of the
     * ItemDomainCableDesignWizardClient using no ops.
     */
    public ItemDomainCableDesignWizard() {
        // "empty" lambda implementation of ItemDomainCableDesignWizardClient cleanupCableWizard() method
        client = (() -> {}); 
    }

    /**
     * Creates new instance with specified client.  Methods in
     * ItemDomainCableDesignWizardClient interface will be invoked on client.
     * 
     * @param aClient The client, which must implement ItemDomainCableDesignWizardClient
     * interface.
     */
     public ItemDomainCableDesignWizard(ItemDomainCableDesignWizardClient aClient) {
        client = aClient;
    }

    /**
     * Returns the root node of the machine design tree that is used to populate
     * the wizard's endpoint selection tab.
     */
    public TreeNode getMachineDesignTree() {
        return machineDesignTree;
    }

    /**
     * @link ItemDomainCableDesignWizard#getMachineDesignTree 
     */
    public void setMachineDesignTree(TreeNode machineDesignTree) {
        this.machineDesignTree = machineDesignTree;
    }

    /**
     * Returns the cable name.  This is the model for the name input on the
     * "basics" tab.
     */
    public String getName() {
        return name;
    }

    /**
     * @link ItemDomainCableDesignWizard#getName 
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Returns the cable's first endpoint, intended to be set by the client
     * after creating an instance of this class.
     */
    public TreeNode getEndpoint1() {
        return endpoint1;
    }

    /**
     * @link ItemDomainCableDesignWizard#getEndpoint1 
     */
    public void setEndpoint1(TreeNode endpoint1) {
        this.endpoint1 = endpoint1;
    }
    
    /**
     * Returns endpoint1 as a string. 
     * @link ItemDomainCableDesignWizard#getEndpoint1 
     */
    public String getEndpoint1String() {
        if (endpoint1 == null) {
            return new String();
        } else {
            return ((ItemElement)(endpoint1.getData())).getContainedItem().toString();
        }
    }

    /**
     * Returns the cable's second endpoint.  This is set by the wizard's
     * endpoint selection tab, and is the selection model for the machine design
     * tree table.
     */
    public TreeNode getSelectedEndpoint() {
        return selectedEndpoint;
    }
    
    public String getSelectedEndpointString() {
        if (selectedEndpoint == null) {
            return new String();
        } else {
            return ((ItemElement)(selectedEndpoint.getData())).getContainedItem().toString();
        } 
    }

    /**
     * @link ItemDomainCableDesignWizard#getSelectedEndpoint 
     */
    public void setSelectedEndpoint(TreeNode selectedEndpoint) {
        this.selectedEndpoint = selectedEndpoint;
    }

    /**
     * Returns the logical cable type (e.g., placeholder, catalog, bundle, virtual),
     * not to be confused with the cable catalog item for the cable design object
     * that will be created by this wizard (in that case, the cable type is
     * "catalog").  This is the model for radio buttons on the wizard's cable
     * type tab.
     */
    public String getCableType() {
        return cableType;
    }

    /**
     * @link ItemDomainCableDesignWizard#getCableType 
     */
    public void setCableType(String cableType) {
        this.cableType = cableType;
    }

    /**
     * Returns the selection model for the cable catalog data table.
     */
    public Item getSelectedCableCatalogItem() {
        return selectedCableCatalogItem;
    }

    /**
     * @link ItemDomainCableDesignWizard#getSelectedCableCatalogItem 
     */
    public void setSelectedCableCatalogItem(Item selectedCableCatalogItem) {
        this.selectedCableCatalogItem = selectedCableCatalogItem;
    }
    
    /**
     * Handles FlowEvents generated by the wizard component.
     */
    public String onFlowProcess(FlowEvent event) {        
        return event.getNewStep();
    }
    
    /**
     * Implements the cancel operation, invoked by the wizard's "Cancel"
     * navigation button.
     */
    public void cancel() {
        client.cleanupCableWizard();
    }
    
    /**
     * Implements the save operation, invoked by the wizard's "Save" navigation
     * button.
     */
    public void save() {
        client.cleanupCableWizard();
    }

}
