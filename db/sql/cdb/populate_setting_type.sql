LOCK TABLES `setting_type` WRITE;
/*!40000 ALTER TABLE `setting_type` DISABLE KEYS */;
INSERT INTO `setting_type` (`name`, `description`, `default_value`) VALUES
('AllowedPropertyValue.List.Display.Description','Display allowed property value description.','false'),
('AllowedPropertyValue.List.Display.Id','Display allowed property value id.','false'),
('AllowedPropertyValue.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('AllowedPropertyValue.List.Display.SortOrder','Display allowed property value sort order.','true'),
('AllowedPropertyValue.List.Display.Units','Display allowed property value units.','true'),
('AllowedPropertyValue.List.FilterBy.Description','Filter for allowed property value description.',NULL),
('AllowedPropertyValue.List.FilterBy.SortOrder','Filter for allowed property value class sort order.',NULL),
('AllowedPropertyValue.List.FilterBy.Units','Filter for allowed property value units.',NULL),
('AllowedPropertyValue.List.FilterBy.Value','Filter for allowed property value.',NULL),
('Component.List.Display.Category','Display component type category.','true'),
('Component.List.Display.CreatedByUser','Display created by username.','false'),
('Component.List.Display.CreatedOnDateTime','Display created on date/time.','false'),
('Component.List.Display.Description','Display component description.','true'),
('Component.List.Display.Id','Display component id.','false'),
('Component.List.Display.LastModifiedByUser','Display last modified by username.','false'),
('Component.List.Display.LastModifiedOnDateTime','Display last modified on date/time.','false'),
('Component.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('Component.List.Display.OwnerUser','Display owner username.','true'),
('Component.List.Display.OwnerGroup','Display owner group name.','true'),
('Component.List.Display.PropertyTypeId1','Display property value for property type id #1.','1'),
('Component.List.Display.PropertyTypeId2','Display property value for property type id #2.',''),
('Component.List.Display.PropertyTypeId3','Display property value for property type id #3.',''),
('Component.List.Display.PropertyTypeId4','Display property value for property type id #4.',''),
('Component.List.Display.PropertyTypeId5','Display property value for property type id #5.',''),
('Component.List.Display.Sources','Display component sources.','true'),
('Component.List.Display.Type','Display component type.','true'),
('Component.List.FilterBy.Category','Filter for components by type category.',NULL),
('Component.List.FilterBy.CreatedByUser','Filter for components that were created by username.',NULL),
('Component.List.FilterBy.CreatedOnDateTime','Filter for components that were created on date/time.',NULL),
('Component.List.FilterBy.Description','Filter for components by description.',NULL),
('Component.List.FilterBy.LastModifiedByUser','Filter for components that were last modified by username.',NULL),
('Component.List.FilterBy.LastModifiedOnDateTime','Filter for components that were last modified on date/time.',NULL),
('Component.List.FilterBy.PropertyValue1','Filter for property value with displayed property type id #1.',''),
('Component.List.FilterBy.PropertyValue2','Filter for property value with displayed property type id #2.',''),
('Component.List.FilterBy.PropertyValue3','Filter for property value with displayed property type id #3.',''),
('Component.List.FilterBy.PropertyValue4','Filter for property value with displayed property type id #4.',''),
('Component.List.FilterBy.PropertyValue5','Filter for property value with displayed property type id #5.',''),
('Component.List.FilterBy.Name','Filter for components by name.',NULL),
('Component.List.FilterBy.OwnerUser','Filter for components by owner username.',NULL),
('Component.List.FilterBy.OwnerGroup','Filter for components by owner group name.',NULL),
('Component.List.FilterBy.Sources','Filter for components by sources.',NULL),
('Component.List.FilterBy.Type','Filter for components by type.',NULL),
('ComponentInstance.List.Display.CreatedByUser','Display created by username.','false'),
('ComponentInstance.List.Display.CreatedOnDateTime','Display created on date/time.','false'),
('ComponentInstance.List.Display.Description','Display component instance description.','true'),
('ComponentInstance.List.Display.Id','Display component instance id.','false'),
('ComponentInstance.List.Display.LastModifiedByUser','Display last modified by username.','false'),
('ComponentInstance.List.Display.LastModifiedOnDateTime','Display last modified on date/time.','false'),
('ComponentInstance.List.Display.LocationDetails','Display component instance location details.','false'),
('ComponentInstance.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('ComponentInstance.List.Display.OwnerUser','Display owner username.','true'),
('ComponentInstance.List.Display.OwnerGroup','Display owner group name.','true'),
('ComponentInstance.List.Display.PropertyTypeId1','Display property value for property type id #1.',''),
('ComponentInstance.List.Display.PropertyTypeId2','Display property value for property type id #2.',''),
('ComponentInstance.List.Display.PropertyTypeId3','Display property value for property type id #3.',''),
('ComponentInstance.List.Display.PropertyTypeId4','Display property value for property type id #4.',''),
('ComponentInstance.List.Display.PropertyTypeId5','Display property value for property type id #5.',''),
('ComponentInstance.List.Display.QrId','Display component instance QR id.','true'),
('ComponentInstance.List.Display.SerialNumber','Display component instance serial number.','false'),
('ComponentInstance.List.FilterBy.CreatedByUser','Filter for components that were created by username.',NULL),
('ComponentInstance.List.FilterBy.CreatedOnDateTime','Filter for components that were created on date/time.',NULL),
('ComponentInstance.List.FilterBy.Description','Filter for components by description.',NULL),
('ComponentInstance.List.FilterBy.LastModifiedByUser','Filter for components that were last modified by username.',NULL),
('ComponentInstance.List.FilterBy.LastModifiedOnDateTime','Filter for components that were last modified on date/time.',NULL),
('ComponentInstance.List.FilterBy.Location','Filter for component instance location.',NULL),
('ComponentInstance.List.FilterBy.LocationDetails','Filter for component instance location details.',NULL),
('ComponentInstance.List.FilterBy.OwnerUser','Filter for component instances by owner username.',NULL),
('ComponentInstance.List.FilterBy.OwnerGroup','Filter for component instances by owner group name.',NULL),
('ComponentInstance.List.FilterBy.PropertyValue1','Filter for property value with displayed property type id #1.',''),
('ComponentInstance.List.FilterBy.PropertyValue2','Filter for property value with displayed property type id #2.',''),
('ComponentInstance.List.FilterBy.PropertyValue3','Filter for property value with displayed property type id #3.',''),
('ComponentInstance.List.FilterBy.PropertyValue4','Filter for property value with displayed property type id #4.',''),
('ComponentInstance.List.FilterBy.PropertyValue5','Filter for property value with displayed property type id #5.',''),
('ComponentInstance.List.FilterBy.QrId','Filter for component instance QR id.',NULL),
('ComponentInstance.List.FilterBy.SerialNumber','Filter for component instance serial number.',NULL),
('ComponentInstance.List.FilterBy.Tag','Filter for component instance tag.',NULL),
('ComponentSource.List.Display.ContactInfo','Display component source contact infpo.','false'),
('ComponentSource.List.Display.Cost','Display component cost.','true'),
('ComponentSource.List.Display.Description','Display component source description.','true'),
('ComponentSource.List.Display.Id','Display component source id.','false'),
('ComponentSource.List.Display.IsManufacturer','Display component source manufacturer designation.','true'),
('ComponentSource.List.Display.IsVendor','Display component source vendor designation.','true'),
('ComponentSource.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('ComponentSource.List.Display.PartNumber','Display component part number.','true'),
('ComponentSource.List.Display.Url','Display component source URL.','false'),
('ComponentSource.List.FilterBy.ContactInfo','Filter for component sources by contact info.',NULL),
('ComponentSource.List.FilterBy.Cost','Filter for component sources by cost.',NULL),
('ComponentSource.List.FilterBy.Description','Filter for component sources by description.',NULL),
('ComponentSource.List.FilterBy.IsManufacturer','Filter for component sources by manufacturer designation.',NULL),
('ComponentSource.List.FilterBy.IsVendor','Filter for component sources by vendor designation.',NULL),
('ComponentSource.List.FilterBy.PartNumber','Filter for component sources by part number.',NULL),
('ComponentSource.List.FilterBy.SourceName','Filter for component sources by name.',NULL),
('ComponentSource.List.FilterBy.Url','Filter for component sources by URL.',NULL),
('ComponentType.List.Display.Category','Display component type category.','true'),
('ComponentType.List.Display.Description','Display component type description.','true'),
('ComponentType.List.Display.Id','Display component type id.','false'),
('ComponentType.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('ComponentType.List.FilterBy.Category','Filter for component type category.',NULL),
('ComponentType.List.FilterBy.Description','Filter for component type description.',NULL),
('ComponentType.List.FilterBy.Name','Filter for component type name.',NULL),
('ComponentTypeCategory.List.Display.Description','Display component type category description.','true'),
('ComponentTypeCategory.List.Display.Id','Display component type category id.','false'),
('ComponentTypeCategory.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('ComponentTypeCategory.List.FilterBy.Description','Filter for component type category description.',NULL),
('ComponentTypeCategory.List.FilterBy.Name','Filter for component type category name.',NULL),
('ComponentTypePropertyType.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('ComponentTypePropertyType.List.Display.Id','Display component type property type id.','false'),
('ComponentTypePropertyType.List.FilterBy.PropertyTypeName','Filter for component type property type name.',NULL),
('Design.List.Display.CreatedByUser','Display created by username.','false'),
('Design.List.Display.CreatedOnDateTime','Display created on date/time.','false'),
('Design.List.Display.Description','Display design description.','true'),
('Design.List.Display.FlatTableView','Display flat table view for design list.','false'),
('Design.List.Display.Id','Display design id.','false'),
('Design.List.Display.LastModifiedByUser','Display last modified by username.','false'),
('Design.List.Display.LastModifiedOnDateTime','Display last modified on date/time.','false'),
('Design.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('Design.List.Display.OwnerUser','Display owner username.','true'),
('Design.List.Display.OwnerGroup','Display owner group name.','true'),
('Design.List.FilterBy.CreatedByUser','Filter for designs that were created by username.',NULL),
('Design.List.FilterBy.CreatedOnDateTime','Filter for designs that were created on date/time.',NULL),
('Design.List.FilterBy.Description','Filter for designs by description.',NULL),
('Design.List.FilterBy.LastModifiedByUser','Filter for designs that were last modified by username.',NULL),
('Design.List.FilterBy.LastModifiedOnDateTime','Filter for designs that were last modified on date/time.',NULL),
('Design.List.FilterBy.Name','Filter for designs by name.',NULL),
('Design.List.FilterBy.OwnerUser','Filter for designs by owner username.',NULL),
('Design.List.FilterBy.OwnerGroup','Filter for designs by owner group name.',NULL),
('DesignElement.List.Display.ChildDesign','Display child design.','true'),
('DesignElement.List.Display.Component','Display component.','true'),
('DesignElement.List.Display.CreatedByUser','Display created by username.','false'),
('DesignElement.List.Display.CreatedOnDateTime','Display created on date/time.','false'),
('DesignElement.List.Display.Description','Display design element description.','false'),
('DesignElement.List.Display.FlatTableView','Display flat table view for design element list.','false'),
('DesignElement.List.Display.Id','Display design element id.','false'),
('DesignElement.List.Display.LastModifiedByUser','Display last modified by username.','false'),
('DesignElement.List.Display.LastModifiedOnDateTime','Display last modified on date/time.','false'),
('DesignElement.List.Display.Location','Display location.','true'),
('DesignElement.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('DesignElement.List.Display.OwnerUser','Display owner username.','true'),
('DesignElement.List.Display.OwnerGroup','Display owner group name.','true'),
('DesignElement.List.Display.SortOrder','Display design element sort order.','true'),
('DesignElement.List.FilterBy.ChildDesign','Filter for child design.',NULL),
('DesignElement.List.FilterBy.Component','Filter for component.',NULL),
('DesignElement.List.FilterBy.CreatedByUser','Filter for design elements that were created by username.',NULL),
('DesignElement.List.FilterBy.CreatedOnDateTime','Filter for design elements that were created on date/time.',NULL),
('DesignElement.List.FilterBy.Description','Filter for design elements by description.',NULL),
('DesignElement.List.FilterBy.LastModifiedByUser','Filter for design elements that were last modified by username.',NULL),
('DesignElement.List.FilterBy.LastModifiedOnDateTime','Filter for design elements that were last modified on date/time.',NULL),
('DesignElement.List.FilterBy.Location','Filter for component.',NULL),
('DesignElement.List.FilterBy.Name','Filter for design elements by name.',NULL),
('DesignElement.List.FilterBy.OwnerUser','Filter for design elements by owner username.',NULL),
('DesignElement.List.FilterBy.OwnerGroup','Filter for design elements by owner group name.',NULL),
('DesignElement.List.FilterBy.SortOrder','Filter for design elements by sort order.',NULL),
('DesignLink.List.Display.Description','Display design link description.','false'),
('DesignLink.List.Display.Id','Display design link id.','false'),
('DesignLink.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('DesignLink.List.Display.Tag','Display design link tag.','true'),
('Location.List.Display.Description','Display location description.','true'),
('Location.List.Display.FlatTableView','Display flat table view for location list.','false'),
('Location.List.Display.Id','Display location id.','false'),
('Location.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('Location.List.Display.Parent','Display location parent.','true'),
('Location.List.Display.Type','Display location type.','true'),
('Location.List.FilterBy.Description','Filter for location type description.',NULL),
('Location.List.FilterBy.Name','Filter for location type name.',NULL),
('Location.List.FilterBy.Parent','Filter for location parent.',NULL),
('Location.List.FilterBy.Type','Filter for location type.',NULL),
('LocationType.List.Display.Description','Display location type description.','true'),
('LocationType.List.Display.Id','Display location type id.','false'),
('LocationType.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('LocationType.List.FilterBy.Description','Filter for location type description.',NULL),
('LocationType.List.FilterBy.Name','Filter for location type name.',NULL),
('Log.List.Display.Attachments','Display log entry attachments.','true'),
('Log.List.Display.EnteredOnDateTime','Display log entry entered on date/time.','true'),
('Log.List.Display.EnteredByUser','Display log entry entered by user.','true'),
('Log.List.Display.Id','Display log entry id.','false'),
('Log.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('Log.List.Display.Topic','Display log topic.','false'),
('Log.List.FilterBy.EnteredOnDateTime','Filter for log entry entered on date/time.',NULL),
('Log.List.FilterBy.EnteredByUser','Filter for log entry entered by user.',NULL),
('Log.List.FilterBy.Text','Filter for log entry text.',NULL),
('Log.List.FilterBy.Topic','Filter for log topic.',NULL),
('PropertyType.List.Display.Category','Display property type category.','true'),
('PropertyType.List.Display.DefaultUnits','Display property type default units.','false'),
('PropertyType.List.Display.DefaultValue','Display property type default value.','false'),
('PropertyType.List.Display.Description','Display property type description.','true'),
('PropertyType.List.Display.Handler','Display property type class handler.','true'),
('PropertyType.List.Display.Id','Display property type id.','false'),
('PropertyType.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('PropertyType.List.FilterBy.Category','Filter for property type category.',NULL),
('PropertyType.List.FilterBy.DefaultUnits','Filter for property type default units.',NULL),
('PropertyType.List.FilterBy.DefaultValue','Filter for property type default value.',NULL),
('PropertyType.List.FilterBy.Description','Filter for property type description.',NULL),
('PropertyType.List.FilterBy.Handler','Filter for property type class handler.',NULL),
('PropertyType.List.FilterBy.Name','Filter for property type name.',NULL),
('PropertyTypeCategory.List.Display.Description','Display property type category description.','true'),
('PropertyTypeCategory.List.Display.Id','Display property type category id.','false'),
('PropertyTypeCategory.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('PropertyTypeCategory.List.FilterBy.Description','Filter for property type category description.',NULL),
('PropertyTypeCategory.List.FilterBy.Name','Filter for property type category name.',NULL),
('PropertyTypeHandler.List.Display.Description','Display property type handler description.','true'),
('PropertyTypeHandler.List.Display.Id','Display property type handler id.','false'),
('PropertyTypeHandler.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('PropertyTypeHandler.List.FilterBy.Description','Filter for property type handler description.',NULL),
('PropertyTypeHandler.List.FilterBy.Name','Filter for property type handler name.',NULL),
('PropertyValue.List.Display.Description','Display value entry description.','false'),
('PropertyValue.List.Display.EnteredOnDateTime','Display value entry entered on date/time.','false'),
('PropertyValue.List.Display.EnteredByUser','Display value entry entered by user.','false'),
('PropertyValue.List.Display.Id','Display property value entry id.','false'),
('PropertyValue.List.Display.IsDynamic','Display dynamic property type designation.','true'),
('PropertyValue.List.Display.IsUserWriteable','Display user-writeable property type designation.','false'),
('PropertyValue.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('PropertyValue.List.Display.Tag','Display property value tag.','true'),
('PropertyValue.List.Display.TypeCategory','Display property value type category.','false'),
('PropertyValue.List.Display.Units','Display value units.','true'),
('PropertyValue.List.FilterBy.Description','Filter for value description.',NULL),
('PropertyValue.List.FilterBy.EnteredOnDateTime','Filter for value entry entered on date/time.',NULL),
('PropertyValue.List.FilterBy.EnteredByUser','Filter for value entry entered by user.',NULL),
('PropertyValue.List.FilterBy.IsDynamic','Filter for dynamic property value designation.',NULL),
('PropertyValue.List.FilterBy.IsUserWriteable','Filter for user-writeable property value designation.',NULL),
('PropertyValue.List.FilterBy.Tag','Filter for property value tag.',NULL),
('PropertyValue.List.FilterBy.Type','Filter for property value type.',NULL),
('PropertyValue.List.FilterBy.TypeCategory','Filter for property value type category.',NULL),
('PropertyValue.List.FilterBy.Units','Filter for value units.',NULL),
('PropertyValue.List.FilterBy.Value','Filter for value entry.',NULL),
('PropertyValueHistory.List.Display.Description','Display value entry description.','true'),
('PropertyValueHistory.List.Display.EnteredOnDateTime','Display value entry entered on date/time.','true'),
('PropertyValueHistory.List.Display.EnteredByUser','Display value entry entered by user.','true'),
('PropertyValueHistory.List.Display.Id','Display property value entry id.','false'),
('PropertyValueHistory.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('PropertyValueHistory.List.Display.Tag','Display value tag.','true'),
('PropertyValueHistory.List.Display.Units','Display value units.','true'),
('PropertyValueHistory.List.FilterBy.Description','Filter for value description.',NULL),
('PropertyValueHistory.List.FilterBy.EnteredOnDateTime','Filter for value entry entered on date/time.',NULL),
('PropertyValueHistory.List.FilterBy.EnteredByUser','Filter for value entry entered by user.',NULL),
('PropertyValueHistory.List.FilterBy.Tag','Filter for value tag.',NULL),
('PropertyValueHistory.List.FilterBy.Units','Filter for value units.',NULL),
('PropertyValueHistory.List.FilterBy.Value','Filter for value entry.',NULL),
('Search.CaseInsensitive','Case insensitive search.','true'),
('Search.Display.Components','Display search result for components.','true'),
('Search.Display.ComponentInstances','Display search result for component instances.','true'),
('Search.Display.ComponentTypes','Display search result for component types.','true'),
('Search.Display.ComponentTypeCategories','Display search result for component type categories.','true'),
('Search.Display.Designs','Display search result for designs.','true'),
('Search.Display.DesignElements','Display search result for design elements.','true'),
('Search.Display.Locations','Display search result for locations.','true'),
('Search.Display.LocationTypes','Display search result for location types.','true'),
('Search.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('Search.Display.PropertyTypes','Display search result for property types.','true'),
('Search.Display.PropertyTypeCategories','Display search result for property type categories.','true'),
('Search.Display.Sources','Display search result for sources.','true'),
('Search.Display.Users','Display search result for users.','true'),
('Search.Display.UserGroups','Display search result for user groups.','true'),
('Source.List.Display.ContactInfo','Display source contact info.','true'),
('Source.List.Display.Description','Display source description.','true'),
('Source.List.Display.Url','Display source URL.','true'),
('Source.List.Display.Id','Display source id.','false'),
('Source.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('Source.List.FilterBy.ContactInfo','Filter for source contact info.',NULL),
('Source.List.FilterBy.Description','Filter for source description.',NULL),
('Source.List.FilterBy.Name','Filter for source name.',NULL),
('Source.List.FilterBy.Url','Filter for source URL.',NULL),
('UserInfo.List.Display.Description','Display user description.','false'),
('UserInfo.List.Display.Email','Display user email.','true'),
('UserInfo.List.Display.FirstName','Display user first name.','true'),
('UserInfo.List.Display.Id','Display user id.','false'),
('UserInfo.List.Display.Groups','Display user groups.','true'),
('UserInfo.List.Display.LastName','Display user last name.','true'),
('UserInfo.List.Display.MiddleName','Display user middle name.','false'),
('UserInfo.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('UserInfo.List.FilterBy.Description','Filter for user description.',NULL),
('UserInfo.List.FilterBy.Email','Filter for user email.',NULL),
('UserInfo.List.FilterBy.FirstName','Filter for user first name.',NULL),
('UserInfo.List.FilterBy.Groups','Filter for user groups.',NULL),
('UserInfo.List.FilterBy.LastName','Filter for user last name.',NULL),
('UserInfo.List.FilterBy.MiddleName','Filter for user middle name.',NULL),
('UserInfo.List.FilterBy.Username','Filter for username.',NULL),
('UserGroup.List.Display.Description','Display user group description.','true'),
('UserGroup.List.Display.Id','Display user group id.','false'),
('UserGroup.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25'),
('UserGroup.List.FilterBy.Description','Filter for user group description.',NULL),
('UserGroup.List.FilterBy.Name','Filter for user group name.',NULL),
('UserSetting.List.Display.NumberOfItemsPerPage','Display specified number of items per page.','25');
/*!40000 ALTER TABLE `setting_type` ENABLE KEYS */;
UNLOCK TABLES;
