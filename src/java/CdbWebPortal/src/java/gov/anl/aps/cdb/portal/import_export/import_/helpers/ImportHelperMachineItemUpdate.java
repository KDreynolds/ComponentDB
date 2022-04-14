/*
 * Copyright (c) UChicago Argonne, LLC. All rights reserved.
 * See LICENSE file.
 */
package gov.anl.aps.cdb.portal.import_export.import_.helpers;

import gov.anl.aps.cdb.common.exceptions.CdbException;
import gov.anl.aps.cdb.portal.controllers.ItemDomainMachineDesignController;
import gov.anl.aps.cdb.portal.controllers.utilities.ItemDomainMachineDesignControllerUtility;
import gov.anl.aps.cdb.portal.import_export.import_.objects.ColumnModeOptions;
import gov.anl.aps.cdb.portal.import_export.import_.objects.HelperWizardOption;
import gov.anl.aps.cdb.portal.import_export.import_.objects.MachineImportHelperCommon;
import static gov.anl.aps.cdb.portal.import_export.import_.objects.MachineImportHelperCommon.KEY_ASSEMBLY_PART;
import static gov.anl.aps.cdb.portal.import_export.import_.objects.MachineImportHelperCommon.KEY_ASSIGNED_ITEM;
import gov.anl.aps.cdb.portal.import_export.import_.objects.ValidInfo;
import gov.anl.aps.cdb.portal.import_export.import_.objects.ValidWarningInfo;
import gov.anl.aps.cdb.portal.import_export.import_.objects.specs.ColumnSpec;
import gov.anl.aps.cdb.portal.model.ItemDomainMachineDesignTreeNode;
import gov.anl.aps.cdb.portal.model.db.entities.Item;
import gov.anl.aps.cdb.portal.model.db.entities.ItemDomainMachineDesign;
import gov.anl.aps.cdb.portal.model.db.entities.ItemElement;
import gov.anl.aps.cdb.portal.model.db.entities.UserInfo;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 *
 * @author craig
 */
public class ImportHelperMachineItemUpdate extends ImportHelperBase<ItemDomainMachineDesign, ItemDomainMachineDesignController> {

    public static final String PROPERTY_PARENT = "importParent";
    
    private MachineImportHelperCommon machineImportHelperCommon = null;
    
    private ItemDomainMachineDesignControllerUtility controllerUtility = null;
    
    private Map<Integer, ItemDomainMachineDesign> itemMap = new HashMap<>();
    private List<ItemDomainMachineDesign> itemList = new ArrayList<>();
    
    private MachineImportHelperCommon getMachineImportHelperCommon() {
        if (machineImportHelperCommon == null) {
            machineImportHelperCommon = new MachineImportHelperCommon();
        }
        return machineImportHelperCommon;
    }
    
    public String getOptionExportNumLevels() {
        return getMachineImportHelperCommon().getOptionExportNumLevels();
    }

    public void setOptionExportNumLevels(String numLevels) {
        getMachineImportHelperCommon().setOptionExportNumLevels(numLevels);
    }
    
    @Override
    protected List<HelperWizardOption> initializeExportWizardOptions() {        
        List<HelperWizardOption> options = new ArrayList<>();        
        options.add(MachineImportHelperCommon.optionExportNumLevels());
        return options;
    }

    @Override
    public ValidInfo validateExportWizardOptions() {
        return HelperWizardOption.validateIntegerOption(
                getMachineImportHelperCommon().getOptionExportNumLevels(),
                MachineImportHelperCommon.OPTION_EXPORT_NUM_LEVELS);
    }
    
    @Override
    public List<ItemDomainMachineDesign> generateExportEntityList_() {
        
        Integer numLevels = null;
        String optionVal = getOptionExportNumLevels();
        if ((optionVal != null) && (!optionVal.isBlank())) {
            numLevels = Integer.valueOf(optionVal);
        }

        ItemDomainMachineDesignTreeNode currentTree = 
                getEntityController().getCurrentMachineDesignListRootTreeNode();
        // List<ItemDomainMachineDesign> filteredItems = currentTree.getFilterResults();

        // create list from tree node hierarchy
        List<ItemDomainMachineDesign> entityList = 
                ItemDomainMachineDesignController.createListForTreeNodeHierarchy(
                        currentTree,
                        numLevels != null,
                        numLevels);
        
        return entityList;
    }

    @Override
    protected List<ColumnSpec> initColumnSpecs() {

        List<ColumnSpec> specs = new ArrayList<>();

        specs.add(existingItemIdColumnSpec());
        specs.add(deleteExistingItemColumnSpec());
        
        specs.add(MachineImportHelperCommon.existingMachineItemColumnSpec(
                ColumnModeOptions.rUPDATErCOMPARE(),
                getMachineImportHelperCommon().getRootItem(),
                null,
                PROPERTY_PARENT,
                "setImportParent",
                "getImportParentPath"));
        
        specs.add(MachineImportHelperCommon.nameColumnSpec(ColumnModeOptions.rUPDATE()));
        specs.add(MachineImportHelperCommon.altNameColumnSpec(ColumnModeOptions.oUPDATE()));
        specs.add(MachineImportHelperCommon.descriptionColumnSpec(ColumnModeOptions.oUPDATE()));
        specs.add(MachineImportHelperCommon.sortOrderColumnSpec(ColumnModeOptions.oUPDATE()));
        specs.add(MachineImportHelperCommon.assignedItemColumnSpec(ColumnModeOptions.oUPDATE()));
        specs.add(MachineImportHelperCommon.locationColumnSpec(ColumnModeOptions.oUPDATE()));
        specs.add(MachineImportHelperCommon.isInstalledColumnSpec(ColumnModeOptions.oUPDATE()));
        specs.add(locationDetailsColumnSpec());
        specs.add(projectListColumnSpec());
        specs.add(ownerUserColumnSpec());
        specs.add(ownerGroupColumnSpec());

        return specs;
    }
    
    @Override
    public ItemDomainMachineDesignController getEntityController() {
        return ItemDomainMachineDesignController.getInstance();
    }

    @Override
    public String getFilenameBase() {
        return "Machine Element Update";
    }

    /**
     * Specifies whether helper supports creation of new instances.
     */
    @Override
    public boolean supportsModeCreate() {
        return false;
    }

    /**
     * Specifies whether helper supports updating existing instances.
     */
    @Override
    public boolean supportsModeUpdate() {
        return true;
    }

    /**
     * Specifies whether helper supports deleting existing instances.
     */
    @Override
    public boolean supportsModeDelete() {
        return true;
    }

    @Override
    protected ItemDomainMachineDesign newInvalidUpdateInstance() {
        return getEntityController().createEntityInstance();
    }
    
    private ItemDomainMachineDesignControllerUtility getControllerUtility() {
        if (controllerUtility == null) {
            controllerUtility = new ItemDomainMachineDesignControllerUtility();
        }
        return controllerUtility;
    }

    /**
     * Updates entity for row in spreadsheet. Only the parent item column is dealt
     * with here since the other columns are handled automatically by the framework.
     */
    @Override
    protected ValidInfo updateEntityInstance(
            ItemDomainMachineDesign item, Map<String, Object> rowMap) {
        
        boolean isValid = true;
        String validString = "";
        
        boolean validRow = (boolean) rowMap.get(KEY_IS_VALID);
        if (validRow) {
            
            // retrieve column values
            UserInfo importUser = (UserInfo) rowMap.get(KEY_USER);
            Item newAssignedItem = (Item) rowMap.get(KEY_ASSIGNED_ITEM);
            String assemblyPartName = (String) rowMap.get(KEY_ASSEMBLY_PART);
            if (assemblyPartName != null) {
                assemblyPartName = assemblyPartName.trim();
            }
            Boolean isInstalled = (Boolean) rowMap.get(MachineImportHelperCommon.KEY_INSTALLED);
            Boolean isTemplate = (Boolean) rowMap.get(MachineImportHelperCommon.KEY_IS_TEMPLATE);
            ItemDomainMachineDesign newParentItem = (ItemDomainMachineDesign) rowMap.get(PROPERTY_PARENT);
            
            // validate and handle "assigned item" and "is installed" columns if either has changed
            Boolean itemIsHoused = item.getImportIsInstalled();
            Item oldAssignedItem = item.getAssignedItem();
            if (((itemIsHoused == null && isInstalled != null) || (itemIsHoused != null && isInstalled == null) || (itemIsHoused != null && !itemIsHoused.equals(isInstalled))) 
                    || ((oldAssignedItem == null && newAssignedItem != null) || (oldAssignedItem != null && newAssignedItem == null) || (oldAssignedItem != null && !oldAssignedItem.equals(newAssignedItem)))) {

                ValidInfo assignedItemValidInfo
                        = MachineImportHelperCommon.handleAssignedItem(
                                item, newAssignedItem, assemblyPartName, importUser, isInstalled);
                if (!assignedItemValidInfo.isValid()) {
                    return assignedItemValidInfo;
                }
            }
                    
            // validate move of item from oldParentItem to newParentItem
            ItemDomainMachineDesign oldParentItem = item.getParentMachineDesign();            
            // Ned said to disallow moving to root level for now. For moving to the root level, we'll
            // need to delete the existing ItemElement when we update the item.
            // In the past, similar things have been accomplished by adding the ItemElement
            // to a transient variable list like elementsToCreate/Delete, and then overriding update() in the facade
            // to also create or delete the associated ItemElements in elementsToCreate/Delete.
            if ((newParentItem == null)) {
                if (oldParentItem != null) {
                    isValid = false;
                    validString = "Item cannot be moved to root level of hierarchy";
                }

            } else {
                
                // check to see if parent item changed
                if (!newParentItem.equals(item.getParentMachineDesign())) {
                    UserInfo ownerUser = item.getOwnerUser();
                    ItemElement relationshipElement = null;
                    try {
                        relationshipElement = getControllerUtility().performMachineMove(newParentItem, item, ownerUser);
                        if (oldParentItem == null) {
                            // handle case where moving item from root level of hierarchy, 
                            // need to create new ItemElement for relationship 
                            // between new parent and child in database, so add to collection and
                            // facade will create ItemElement when updating the item.
                            item.getElementsToCreate().add(relationshipElement);
                        }
                    } catch (CdbException ex) {
                        isValid = false;
                        validString = "Exception moving item to new parent: " + ex.getMessage();
                    }
                }
            }
        }
        
        return new ValidInfo(isValid, validString);
    }
    
    @Override
    protected ValidInfo deleteEntityInstance(ItemDomainMachineDesign entity, Map<String, Object> rowMap) {
        
        boolean isValid = true;
        String validStr = "";
        
        ItemDomainMachineDesignController controller = ItemDomainMachineDesignController.getInstance();
        
        // collect list of items to update (mark deleted) and elements (relationships) to delete for this row
        List<ItemDomainMachineDesign> itemsMovingToTrash = new ArrayList<>();
        List<ItemElement> elementsToDelete = new ArrayList<>();
        controller.collectItemsFromHierarchy(entity, itemsMovingToTrash, elementsToDelete, true, true);
        
        // eliminate items already contained in itemMap (e.g., the input spreadsheet might contain overlapping
        // hierarchies with common children where one row is an ancestor of another)
        List<ItemDomainMachineDesign> newItems = new ArrayList<>();
        ItemDomainMachineDesign rootItem = null;
        for (ItemDomainMachineDesign item : itemsMovingToTrash) {
            // save reference to rootItem so that we can update its parent later
            if (item.getId().equals(entity.getId())) {
                rootItem = item;
            }
            // eliminate items we've already processed and update data structures for new items
            if (!itemMap.containsKey(item.getId())) {
                newItems.add(item);
                itemMap.put(item.getId(), item);
                itemList.add(item);
            }
        }
        itemsMovingToTrash = newItems;
        if (rootItem == null) {
            // this shouldn't happen, indicates problem with collectItemsFromHierarchy
            isValid = false;
            validStr = "Unexpected error retrieving children of specified item";
            return new ValidInfo(isValid, validStr);
        }
                
        // validate list of items to move to trash
        ValidWarningInfo info = controller.validateItemsMovingToTrash(itemsMovingToTrash);
        isValid = info.isValid();
        validStr = info.validString();
        validStr = appendToString(validStr, info.warningString());
        
        if (isValid) {
            ValidInfo moveValidInfo = controller.handleMoveToTrash(itemsMovingToTrash, elementsToDelete);
            if (!moveValidInfo.isValid()) {
                isValid = false;
                validStr = appendToString(validStr, moveValidInfo.getValidString());
            }
        }
        
        // Size of list is 1 for interior node, 0 for root node.  Greater than one is an
        // unexpected error handled by handleMoveToTrash().  For interior node, we need to update
        // the parent item since a relationship is removed from it
        if (elementsToDelete.size() == 1) {
            ItemElement ie = elementsToDelete.get(0);
            ItemDomainMachineDesign ieParentItem = (ItemDomainMachineDesign) ie.getParentItem();
            if (ieParentItem != null) {
                rootItem.addItemToUpdate(ieParentItem);
            }
        }
        
        return new ValidInfo(isValid, validStr);
    }

    /**
     * Override so that we use updateList for persistence moving to trash instead of deleteList
     * which would permanently delete the items.
     */
    protected void deleteList() throws CdbException, RuntimeException {

        List<ItemDomainMachineDesign> deleteEntities = new ArrayList<>();
        for (ItemDomainMachineDesign entity : rows) {
            if (entity.getImportDeleteExistingItem()) {
                deleteEntities.add(entity);
            }
        }

        ItemDomainMachineDesignController controller = this.getEntityController();
        if (!deleteEntities.isEmpty()) {
            controller.updateList(deleteEntities, getCreateMessageTypeName());
        }
    }
}
